import asyncio
import websockets
import json
import logging
import traceback
from datetime import datetime
from .models.ticker import BookTicker

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class WsClient:
    URI = ""
    SANDBOX_URI = ""

    def __init__(
        self,
        subscription: dict,
        is_sandbox: bool = False,
        orderbook_queue: asyncio.Queue = None,
        slack=None,
        slack_bot_name: str = None,
        slack_channel_name: str = None,
    ):
        self.uri = self.URI if not is_sandbox else self.SANDBOX_URI
        self.subscription = subscription
        self.orderbook_queue = orderbook_queue
        self.should_run = True
        self.websocket = None

        self.slack = slack
        self.slack_bot_name = slack_bot_name
        self.slack_channel_name = slack_channel_name

        self.message_check_task = None
        self.last_message_time = asyncio.get_event_loop().time()

    async def send_slack(self, msg: str):
        if self.slack and self.slack_bot_name and self.slack_channel_name:
            try:
                await self.slack.send_message(
                    self.slack_bot_name,
                    self.slack_channel_name,
                    f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {msg}",
                )
            except Exception as e:
                logger.warning(f"Slack error: {e}")

    async def on_message(self, message: str):
        logger.info(f"Received message: {message}")

    async def update_orderbook_queue(self, exchange: str, symbol: str, ticker: BookTicker):
        if not self.orderbook_queue:
            return
        await self.orderbook_queue.put(
            (
                exchange,
                symbol,
                ticker,
            )
        )

    async def on_open(self):
        subscribe_message = json.dumps(self.subscription)
        await self.websocket.send(subscribe_message)
        await self.send_slack(f"[INFO] - {self.__class__.__name__} WebSocket connection opened")
        logger.info("WebSocket connection opened")
        logger.info(f"Sent subscription message: {subscribe_message}")

    async def on_close(self):
        logger.info("WebSocket connection closed")
        if self.message_check_task:
            self.message_check_task.cancel()
        await self.send_slack(f"[CRITICAL] - {self.__class__.__name__} WebSocket connection closed")

    async def on_error(self, error: Exception):
        await self.send_slack(f"[CRITICAL] - {self.__class__.__name__} Error occurred: {traceback.format_exc()}")
        await self.reconnect()

    async def message_check_loop(self):
        while self.should_run:
            now = asyncio.get_event_loop().time()
            if now - self.last_message_time > 30:
                await self.send_slack(
                    f"[CRITICAL] - {self.__class__.__name__} No message received for 30 seconds. Reconnecting..."
                )
                await self.reconnect()
                break
            await asyncio.sleep(1)

    async def receive_loop(self):
        first_message = True
        try:
            async for message in self.websocket:
                self.last_message_time = asyncio.get_event_loop().time()

                if first_message:
                    try:
                        parsed = json.loads(message)
                        print("📥 Received first raw message:")
                        print(json.dumps(parsed, indent=2, ensure_ascii=False))
                    except Exception:
                        print("📥 Received non-JSON first message:", message)
                    first_message = False

                await self.on_message(message)
        except Exception as e:
            await self.on_error(e)

    async def connect(self):
        async with websockets.connect(self.uri, ping_interval=10, ping_timeout=3) as ws:
            self.websocket = ws
            await self.on_open()

            try:
                self.message_check_task = asyncio.create_task(self.message_check_loop())
                await self.receive_loop()
            finally:
                await self.on_close()

    async def reconnect(self):
        if self.should_run:
            await self.connect()

    async def send_message(self, message: dict):
        if self.websocket:
            await self.websocket.send(json.dumps(message))
            logger.info(f"Sent message: {message}")
        else:
            logger.warning("WebSocket not connected")

    async def start(self):
        self.should_run = True
        while self.should_run:
            try:
                await self.connect()
            except Exception as e:
                logger.error(f"Connection error: {e}")
                await self.send_slack(
                    f"[CRITICAL] - {self.__class__.__name__}, Connection error: {traceback.format_exc()}"
                )
                await asyncio.sleep(0.1)

    async def stop(self):
        self.should_run = False
        if self.websocket:
            await self.websocket.close()
