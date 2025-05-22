import json
import time
import hmac
import hashlib
import base64
import logging
import polars as pl
from .models.balance import BalanceInfo
from .models.position import PositionInfo, PositionSide
from .base import WsClient
from .data.market_data import MarketData
from .models.ticker import BookTicker
from .models.order import Exchange, OrderStatus, TradeStatus

logger = logging.getLogger(__name__)


def safe_float(value, default=0.0):
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


class OkxPublicWsClient(WsClient):
    URI = "wss://ws.okx.com:8443/ws/v5/public"

    def __init__(
        self,
        subscription: dict,
        is_sandbox: bool = False,
        orderbook_queue=None,
        slack=None,
        slack_bot_name: str = None,
        slack_channel_name: str = None,
    ):
        super().__init__(subscription, is_sandbox, orderbook_queue, slack, slack_bot_name, slack_channel_name)
        self.market_data = MarketData()

    @classmethod
    async def create(cls, **kwargs):
        self = cls(**kwargs)
        return self

    async def on_message(self, message: str):
        await super().on_message(message)
        payload = json.loads(message)

        channel = payload.get("arg", {}).get("channel")
        data = payload.get("data", [])

        if channel == "bbo-tbt" and data:
            data_payload = data[0]
            book_ticker = BookTicker(
                symbol=payload["arg"].get("instId"),
                product_type="SWAP" if payload["arg"].get("instId").endswith("-SWAP") else "SPOT",
                best_bid_price=float(data_payload.get("bids", [[0, 0]])[0][0]),
                best_bid_quantity=float(data_payload.get("bids", [[0, 0]])[0][1]),
                best_ask_price=float(data_payload.get("asks", [[0, 0]])[0][0]),
                best_ask_quantity=float(data_payload.get("asks", [[0, 0]])[0][1]),
                timestamp=int(data_payload.get("ts", 0)),
            )
            await self.market_data.update_depth_data("okx", book_ticker.symbol, book_ticker)
            await self.update_orderbook_queue("okx", book_ticker.symbol, book_ticker)

        elif channel and "candle" in channel and data:
            kline_payload = data[0]
            symbol = payload["arg"].get("instId", "")

            new_df = (
                pl.DataFrame(
                    {
                        "open": [float(kline_payload[1])],
                        "high": [float(kline_payload[2])],
                        "low": [float(kline_payload[3])],
                        "close": [float(kline_payload[4])],
                        "volume": [float(kline_payload[5])],
                        "datetime": [int(kline_payload[0])],
                    }
                )
                .with_columns(pl.col("datetime").cast(pl.Int64).cast(pl.Datetime("ms")))
                .set_sorted("datetime")
            )

            # 直接送到 update_kline_data，由 shared_data 去處理要怎麼存
            await self.market_data.update_kline_data("okx", symbol, new_df)


class OkxPrivateWsClient(WsClient):
    URI = "wss://ws.okx.com:8443/ws/v5/private"

    def __init__(
        self,
        subscription: dict,
        api_key: str,
        api_secret: str,
        passphrase: str,
        is_sandbox: bool = False,
        slack=None,
        slack_bot_name: str = None,
        slack_channel_name: str = None,
    ):
        super().__init__(subscription, is_sandbox, slack, slack_bot_name, slack_channel_name)
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase
        self.market_data = MarketData()

    @classmethod
    async def create(cls, **kwargs):
        self = cls(**kwargs)
        return self

    def sign(self):
        timestamp = str(time.time())
        message = timestamp + "GET" + "/users/self/verify"
        mac = hmac.new(self.api_secret.encode(), message.encode(), hashlib.sha256)
        sign = base64.b64encode(mac.digest()).decode()
        return {
            "op": "login",
            "args": [
                {
                    "apiKey": self.api_key,
                    "passphrase": self.passphrase,
                    "timestamp": timestamp,
                    "sign": sign,
                }
            ],
        }

    async def on_open(self):
        await super().on_open()

        sign_message = json.dumps(self.sign())
        await self.websocket.send(sign_message)

        while True:
            message = await self.websocket.recv()
            payload = json.loads(message)
            if payload.get("event") == "login" and payload.get("code") == "0":
                break
            logger.debug(f"Waiting for login confirmation: {payload}")

        subscribe_message = json.dumps(self.subscription)
        await self.websocket.send(subscribe_message)
        logger.info(f"Sent subscription message: {subscribe_message}")

    async def on_message(self, message: str):
        await super().on_message(message)
        payload = json.loads(message)

        channel = payload.get("arg", {}).get("channel")
        data = payload.get("data", [])

        if channel == "orders" and data:
            for order_data in data:
                try:
                    status_mapping = {
                        "live": OrderStatus.OPEN,
                        "partially_filled": OrderStatus.PARTIALLY_FILLED,
                        "filled": OrderStatus.FILLED,
                        "canceled": OrderStatus.CANCELLED,
                    }
                    trade_status = TradeStatus(
                        order_id=order_data["ordId"],
                        client_oid=order_data["clOrdId"],
                        order_type=order_data["ordType"],
                        status=status_mapping.get(order_data["state"], OrderStatus.OPEN),
                        price=float(order_data.get("px", 0.0)),
                        quantity=float(order_data.get("sz", 0.0)),
                        filled_quantity=float(order_data.get("fillSz", 0.0)),
                        deal_avg_price=float(order_data.get("avgPx", 0.0)),
                    )
                    await self.market_data.update_trade_status(Exchange.OKX, order_data["instId"], trade_status)
                    logger.info(f"Updated TradeStatus: {trade_status}")
                except Exception as e:
                    logger.error(f"Error processing order data: {e}")

        elif channel == "positions" and data:
            for position_data in data:
                try:
                    side_mapping = {
                        "long": PositionSide.LONG,
                        "short": PositionSide.SHORT,
                        "net": PositionSide.NONE,
                    }
                    side = side_mapping.get(position_data["posSide"], PositionSide.NONE)
                    pos_value = float(position_data.get("pos", 0.0))

                    if side == PositionSide.NONE:
                        side = (
                            PositionSide.LONG
                            if pos_value > 0
                            else (PositionSide.SHORT if pos_value < 0 else PositionSide.NONE)
                        )

                    position_info = PositionInfo(
                        symbol=position_data["instId"],
                        side=side,
                        quantity=abs(pos_value),
                        open_avg_price=float(position_data.get("avgPx", 0.0)),
                    )
                    await self.market_data.update_position(Exchange.OKX, position_data["instId"], position_info)
                    logger.info(f"Updated PositionInfo: {position_info}")
                except Exception as e:
                    logger.error(f"Error processing position data: {e}")

        elif channel == "account" and data:
            for balance_data in data:
                try:
                    details = balance_data.get("details", [])
                    for detail in details:
                        balance_info = BalanceInfo(
                            symbol=detail["ccy"],
                            available_balance=safe_float(detail.get("availBal")),
                            position_deposit=safe_float(detail.get("imr")),
                            frozen_balance=safe_float(detail.get("frozenBal")),
                        )
                        await self.market_data.update_balance(Exchange.OKX, detail["ccy"], balance_info)
                        logger.info(f"Updated BalanceInfo: {balance_info}")
                except Exception as e:
                    logger.error(f"Error processing balance data: {e}")
