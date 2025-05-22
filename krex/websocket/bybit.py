import json
import time
import hmac
import logging
import asyncio
import polars as pl
from .base import WsClient
from .data.market_data import MarketData
from .models.balance import BalanceInfo
from .models.order import Exchange, OrderStatus, TradeStatus
from .models.ticker import BookTicker
from .models.position import PositionInfo, PositionSide

logger = logging.getLogger(__name__)


def safe_float(value, default=0.0):
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


class BybitPublicLinearWsClient(WsClient):
    URI = "wss://stream.bybit.com/v5/public/linear"
    SANDBOX_URI = "wss://stream-testnet.bybit.com/v5/public/linear"

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

    async def on_open(self):
        linear_args_plan = [self.subscription["args"][i : i + 10] for i in range(0, len(self.subscription["args"]), 10)]
        for linear_args in linear_args_plan:
            subscribe_message = json.dumps(
                {
                    "op": "subscribe",
                    "args": linear_args,
                }
            )
            await self.websocket.send(subscribe_message)
            logger.info(f"Sent subscription message: {subscribe_message}")
            await asyncio.sleep(0.3)
        await self.send_slack(f"[INFO] - {self.__class__.__name__} WebSocket connection opened")

    async def on_message(self, message: str):
        await super().on_message(message)
        payload = json.loads(message)

        topic = payload.get("topic", "")
        data = payload.get("data", [])

        if topic.startswith("orderbook.1.") and data:
            symbol = topic.split(".")[-1]
            book_ticker = BookTicker(
                symbol=symbol,
                product_type="linear",
                best_bid_price=float(data["b"][0][0]),
                best_bid_quantity=float(data["b"][0][1]),
                best_ask_price=float(data["a"][0][0]),
                best_ask_quantity=float(data["a"][0][1]),
                timestamp=int(payload.get("ts")),
            )
            await self.market_data.update_depth_data("bybit", symbol, book_ticker)
            await self.update_orderbook_queue("bybit", symbol, book_ticker)

        elif topic.startswith("tickers.") and data:
            symbol = topic.split(".")[-1]
            ticker_data = data[0]
            book_ticker = BookTicker(
                symbol=symbol,
                product_type="linear",
                best_bid_price=float(ticker_data["bid1Price"]),
                best_bid_quantity=float(ticker_data["bid1Size"]),
                best_ask_price=float(ticker_data["ask1Price"]),
                best_ask_quantity=float(ticker_data["ask1Size"]),
                timestamp=int(payload.get("ts")),
            )

        elif topic.startswith("kline.") and data:
            kline = data[0]
            symbol = topic.split(".")[-1]

            df = (
                pl.DataFrame(
                    {
                        "open": [float(kline["open"])],
                        "high": [float(kline["high"])],
                        "low": [float(kline["low"])],
                        "close": [float(kline["close"])],
                        "volume": [float(kline["volume"])],
                        "datetime": [int(kline["start"])],
                    }
                )
                .with_columns(pl.col("datetime").cast(pl.Int64).cast(pl.Datetime("ms")))
                .set_sorted("datetime")
            )
            await self.market_data.update_kline_data("bybit", symbol, df)


class BybitPublicSpotWsClient(WsClient):
    URI = "wss://stream.bybit.com/v5/public/spot"
    SANDBOX_URI = "wss://stream-testnet.bybit.com/v5/public/spot"

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

    async def on_open(self):
        spot_args_plan = [self.subscription["args"][i : i + 10] for i in range(0, len(self.subscription["args"]), 10)]
        for spot_args in spot_args_plan:
            subscribe_message = json.dumps(
                {
                    "op": "subscribe",
                    "args": spot_args,
                }
            )
            await self.websocket.send(subscribe_message)
            logger.info(f"Sent subscription message: {subscribe_message}")
            await asyncio.sleep(0.3)
        await self.send_slack(f"[INFO] - {self.__class__.__name__} WebSocket connection opened")

    async def on_message(self, message: str):
        await super().on_message(message)
        payload = json.loads(message)

        topic = payload.get("topic", "")
        data = payload.get("data", [])

        if topic.startswith("orderbook.1.") and data:
            symbol = topic.split(".")[-1]
            book_ticker = BookTicker(
                symbol=symbol,
                product_type="spot",
                best_bid_price=float(data["b"][0][0]),
                best_bid_quantity=float(data["b"][0][1]),
                best_ask_price=float(data["a"][0][0]),
                best_ask_quantity=float(data["a"][0][1]),
                timestamp=int(payload.get("ts")),
            )
            await self.market_data.update_depth_data("bybit", symbol, book_ticker)
            await self.update_orderbook_queue("bybit", symbol, book_ticker)

        elif topic.startswith("tickers.") and data:
            symbol = topic.split(".")[-1]
            ticker_data = data[0]
            book_ticker = BookTicker(
                symbol=symbol,
                product_type="spot",
                best_bid_price=float(ticker_data["bid1Price"]),
                best_bid_quantity=float(ticker_data["bid1Size"]),
                best_ask_price=float(ticker_data["ask1Price"]),
                best_ask_quantity=float(ticker_data["ask1Size"]),
                timestamp=int(payload.get("ts")),
            )
            await self.market_data.update_depth_data("bybit", symbol, book_ticker)

        elif topic.startswith("kline.") and data:
            kline = data[0]
            symbol = topic.split(".")[-1]

            df = (
                pl.DataFrame(
                    {
                        "open": [float(kline["open"])],
                        "high": [float(kline["high"])],
                        "low": [float(kline["low"])],
                        "close": [float(kline["close"])],
                        "volume": [float(kline["volume"])],
                        "datetime": [int(kline["start"])],
                    }
                )
                .with_columns(pl.col("datetime").cast(pl.Int64).cast(pl.Datetime("ms")))
                .set_sorted("datetime")
            )
            await self.market_data.update_kline_data("bybit", symbol, df)


class BybitPrivateWsClient(WsClient):
    URI = "wss://stream.bybit.com/v5/private"
    SANDBOX_URI = "wss://stream-testnet.bybit.com/v5/private"

    def __init__(
        self,
        subscription: dict,
        api_key: str,
        api_secret: str,
        is_sandbox: bool = False,
        slack=None,
        slack_bot_name: str = None,
        slack_channel_name: str = None,
    ):
        super().__init__(subscription, is_sandbox, slack, slack_bot_name, slack_channel_name)
        self.api_key = api_key
        self.api_secret = api_secret
        self.market_data = MarketData()

    @classmethod
    async def create(cls, **kwargs):
        self = cls(**kwargs)
        return self

    def sign(self):
        expires = str(int((time.time() + 60) * 1000))
        message = "GET/realtime" + expires
        signature = hmac.new(self.api_secret.encode("utf-8"), message.encode("utf-8"), digestmod="sha256").hexdigest()
        return {
            "op": "auth",
            "args": [self.api_key, int(expires), signature],
        }

    async def on_open(self):
        await super().on_open()

        sign_message = json.dumps(self.sign())
        await self.websocket.send(sign_message)

        while True:
            message = await self.websocket.recv()
            payload = json.loads(message)
            if payload.get("op") == "auth" and payload.get("success"):
                break
            logger.debug(f"Waiting for auth confirmation: {payload}")

        subscribe_message = json.dumps(self.subscription)
        await self.websocket.send(subscribe_message)
        logger.info(f"Sent subscription message: {subscribe_message}")

    async def on_message(self, message: str):
        await super().on_message(message)
        payload = json.loads(message)

        topic = payload.get("topic", "")
        data = payload.get("data", [])

        if topic == "order" and data:
            for order in data:
                try:
                    trade_status = TradeStatus(
                        order_id=order["orderId"],
                        client_oid=order.get("orderLinkId", ""),
                        order_type=order.get("orderType", ""),
                        status=self.map_order_status(order.get("orderStatus", "")),
                        price=safe_float(order.get("price")),
                        quantity=safe_float(order.get("qty")),
                        filled_quantity=safe_float(order.get("cumExecQty")),
                        deal_avg_price=safe_float(order.get("avgPrice")),
                    )

                    await self.market_data.update_trade_status(Exchange.BYBIT, order["symbol"], trade_status)
                    logger.info(f"Updated TradeStatus: {trade_status}")
                except Exception as e:
                    logger.error(f"Error processing order data: {e}")

        elif topic == "position" and data:
            for position in data:
                try:
                    side = PositionSide.LONG if position.get("side") == "Buy" else PositionSide.SHORT
                    pos_info = PositionInfo(
                        symbol=position["symbol"],
                        side=side,
                        quantity=safe_float(position.get("size")),
                        open_avg_price=safe_float(position.get("entryPrice")),
                    )
                    await self.market_data.update_position(Exchange.BYBIT, position["symbol"], pos_info)
                    logger.info(f"Updated PositionInfo: {pos_info}")
                except Exception as e:
                    logger.error(f"Error processing position data: {e}")

        elif topic == "wallet" and data:
            try:
                wallet = data[0]
                for coin in wallet.get("coin", []):
                    balance_info = BalanceInfo(
                        symbol=coin["coin"],
                        available_balance=safe_float(coin.get("walletBalance")),
                        position_deposit=0.0,
                        frozen_balance=0.0,
                    )
                    await self.market_data.update_balance(Exchange.BYBIT, coin["coin"], balance_info)
                    logger.info(f"Updated BalanceInfo: {balance_info}")
            except Exception as e:
                logger.error(f"Error processing wallet data: {e}")

    def map_order_status(self, status: str):
        mapping = {
            "Created": OrderStatus.OPEN,
            "New": OrderStatus.OPEN,
            "Filled": OrderStatus.FILLED,
            "Cancelled": OrderStatus.CANCELLED,
            "Rejected": OrderStatus.CANCELLED,
            "PartiallyFilled": OrderStatus.PARTIALLY_FILLED,
        }
        return mapping.get(status, OrderStatus.OPEN)
