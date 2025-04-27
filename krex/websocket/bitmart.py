import json
import time
import hmac
import hashlib
import logging
import polars as pl
from krex.async_support.product_table.manager import ProductTableManager
from .models.balance import BalanceInfo
from .base import WsClient
from .data.market_data import MarketData
from .models.ticker import BookTicker
from .models.order import Exchange, OrderStatus, TradeStatus

logger = logging.getLogger(__name__)


class BitmartPublicWsClient(WsClient):
    URI = "wss://openapi-ws-v2.bitmart.com/api?protocol=1.1"
    SANDBOX_URI = ""

    def __init__(
        self,
        subscription: dict,
        api_key: str,
        api_secret: str,
        memo: str,
        is_sandbox: bool = False,
        slack=None,
        slack_bot_name: str = None,
        slack_channel_name: str = None,
    ):
        super().__init__(
            subscription=subscription,
            is_sandbox=is_sandbox,
            slack=slack,
            slack_bot_name=slack_bot_name,
            slack_channel_name=slack_channel_name,
        )
        self.api_key = api_key
        self.api_secret = api_secret
        self.memo = memo

        self.market_data = MarketData()
        self.ptm = None

    @classmethod
    async def create(cls, **kwargs):
        self = cls(**kwargs)
        self.ptm = await ProductTableManager.get_instance()
        return self

    def sign(self):
        timestamp = str(int(time.time() * 1000))
        sign_payload = f"{timestamp}#{self.memo}#bitmart.WebSocket"
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            sign_payload.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return {
            "action": "access",
            "args": [self.api_key, timestamp, signature, "web"],
        }

    async def on_open(self):
        await super().on_open()

        sign_message = json.dumps(self.sign())
        await self.websocket.send(sign_message)

        while True:
            message = await self.websocket.recv()
            payload = json.loads(message)
            if payload.get("action") == "access" and payload.get("success"):
                break
            logger.debug(f"Waiting for access confirmation: {payload}")

        subscribe_message = json.dumps(self.subscription)
        await self.websocket.send(subscribe_message)
        logger.info(f"Sent subscription message: {subscribe_message}")

    async def on_message(self, message: str):
        await super().on_message(message)
        payload = json.loads(message)

        if payload.get("data") and payload.get("group", "").startswith("futures/bookticker:"):
            data_payload = payload["data"]
            data = BookTicker(
                symbol=data_payload.get("symbol", ""),
                best_bid_price=float(data_payload.get("best_bid_price", 0)),
                best_bid_quantity=float(data_payload.get("best_bid_vol", 0)),
                best_ask_price=float(data_payload.get("best_ask_price", 0)),
                best_ask_quantity=float(data_payload.get("best_ask_vol", 0)),
                timestamp=int(data_payload.get("ms_t", 0)),
            )
            await self.market_data.update_depth_data("bitmart", data.symbol, data)

        elif payload.get("data") and payload.get("group") == "futures/order":
            for order_payload in payload["data"]:
                try:
                    order_data = order_payload.get("order", {})
                    state = order_data["state"]
                    size = float(order_data["size"])
                    deal_size = float(order_data["deal_size"])

                    if state == 4:
                        status = OrderStatus.CANCELLED
                    elif deal_size == 0:
                        status = OrderStatus.OPEN
                    elif deal_size == size:
                        status = OrderStatus.FILLED
                    elif size > deal_size:
                        status = OrderStatus.PARTIALLY_FILLED
                    else:
                        status = OrderStatus.OPEN

                    trade_status = TradeStatus(
                        order_id=order_data["order_id"],
                        client_oid=order_data["client_order_id"],
                        order_type=order_data["type"],
                        status=status,
                        price=float(order_data.get("price", 0.0)),
                        quantity=float(order_data.get("size", 0.0)),
                        filled_quantity=float(order_data.get("deal_size", 0.0)),
                        deal_avg_price=float(order_data.get("deal_avg_price", 0.0)),
                    )

                    await self.market_data.update_trade_status(Exchange.BITMART, order_data["symbol"], trade_status)
                    logger.info(f"Updated TradeStatus: {trade_status}")

                except Exception as e:
                    logger.error(f"Error processing order data: {e}")

        elif payload.get("data") and payload.get("group", "").startswith("futures/klineBin"):
            try:
                data_payload = payload["data"]["items"][0]
                df = pl.DataFrame(
                    {
                        "open": [float(data_payload["o"])],
                        "high": [float(data_payload["h"])],
                        "low": [float(data_payload["l"])],
                        "close": [float(data_payload["c"])],
                        "volume": [float(data_payload["v"])],
                        "datetime": [int(data_payload["ts"])],
                    }
                )
                df = df.with_columns([pl.col("datetime").cast(pl.Datetime).dt.cast_time_unit("ms")])
                df = df.set_sorted("datetime")

                product_symbol = self.ptm.get_product_symbol(payload["data"]["symbol"], "bitmart")
                await self.market_data.update_kline_data("bitmart", product_symbol, df)
            except Exception as e:
                logger.error(f"Error processing kline data: {e}")

        elif payload.get("group", "").startswith("futures/asset:"):
            data = payload.get("data")
            try:
                balance_items = data if isinstance(data, list) else [data]
                for item in balance_items:
                    balance_info = BalanceInfo(
                        symbol=item["currency"],
                        available_balance=float(item.get("available_balance", 0.0)),
                        position_deposit=float(item.get("position_deposit", 0.0)),
                        frozen_balance=float(item.get("frozen_balance", 0.0)),
                    )
                    await self.market_data.update_balance(Exchange.BITMART, item["currency"], balance_info)
                    logger.info(f"Updated BalanceInfo: {balance_info}")
            except Exception as e:
                logger.error(f"Error processing balance data: {e}, payload: {payload}")
