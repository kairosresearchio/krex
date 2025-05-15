import asyncio
import websockets
import json
import logging
from datetime import datetime

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
        slack=None,
        slack_bot_name: str = None,
        slack_channel_name: str = None,
    ):
        self.uri = self.URI if not is_sandbox else self.SANDBOX_URI
        self.subscription = subscription
        self.should_run = True
        self.websocket = None

        self.slack = slack
        self.slack_bot_name = slack_bot_name
        self.slack_channel_name = slack_channel_name

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

    async def on_open(self):
        logger.info("WebSocket connection opened")
        await self.send_slack(f"[INFO] - {self.__class__.__name__} WebSocket connection opened")

        subscribe_message = json.dumps(self.subscription)
        await self.websocket.send(subscribe_message)
        logger.info(f"Sent subscription message: {subscribe_message}")

    async def on_close(self):
        logger.info("WebSocket connection closed")
        await self.send_slack(f"[CRITICAL] - {self.__class__.__name__} WebSocket connection closed")

    async def on_error(self, error: Exception):
        logger.error(f"WebSocket error: {error}")
        await self.send_slack(f"[CRITICAL] - {self.__class__.__name__} Error occurred: {error}")

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
        try:
            async with websockets.connect(self.uri, ping_interval=10, ping_timeout=3) as ws:
                self.websocket = ws
                await self.on_open()

                check_task = asyncio.create_task(self.message_check_loop())
                await self.receive_loop()
                check_task.cancel()
        except Exception as e:
            await self.on_error(e)
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
        await self.connect()

    async def stop(self):
        self.should_run = False
        if self.websocket:
            await self.websocket.close()
