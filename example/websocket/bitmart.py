import asyncio
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

from krex.async_support.bitmart.client import Client
from krex.websocket.bitmart import BitmartPublicWsClient
from krex.websocket.data.market_data import MarketData
from krex.websocket.bot.slack import Slack


load_dotenv()


async def initialize(shared_data: MarketData):
    slack = Slack(
        bot_tokens={
            "GHOST": os.getenv("SLACK_BOT_GHOST"),
        },
        channel_ids={
            "CRITICAL": os.getenv("SLACK_CHANNEL_CRITICAL"),
            "ALL_KAIROS": os.getenv("SLACK_CHANNEL_ALL_KAIROS"),
        },
    )

    bitmart_client = Client(
        api_key=os.getenv("BITMART_APIKEY"),
        api_secret=os.getenv("BITMART_APISECRET"),
        memo=os.getenv("BITMART_MEMO"),
    )
    await bitmart_client.async_init()

    kline_df = await bitmart_client.get_contract_kline(
        product_symbol="ETH-USDT-SWAP",
        interval="1m",
        start_time=int((datetime.now() - timedelta(minutes=100)).timestamp()),
        end_time=int(datetime.now().timestamp()),
    )
    await shared_data.update_kline_data("bitmart", "ETH-USDT-SWAP", kline_df)

    ws_client = await BitmartPublicWsClient.create(
        subscription={
            "action": "subscribe",
            "args": [
                "futures/klineBin1m:ETHUSDT",
                "futures/order",
                "futures/bookticker:ETHUSDT",
                "futures/asset:USDT",
            ],
        },
        api_key=os.getenv("BITMART_APIKEY"),
        api_secret=os.getenv("BITMART_APISECRET"),
        memo=os.getenv("BITMART_MEMO"),
        slack=slack,
        slack_bot_name="GHOST",
        slack_channel_name="CRITICAL",
    )
    ws_client.market_data = shared_data

    asyncio.create_task(ws_client.start())

    return ws_client


async def monitor_loop(data: MarketData):
    while True:
        depth_data = await data.get_all_depth_data()
        kline_data = await data.get_all_kline_data()
        trade_data = await data.get_all_trade_statuses()
        balance_data = await data.get_all_balances()

        print("Depth Data:", depth_data)
        print("Kline Data:", kline_data)
        print("Trade Data:", trade_data)
        print("Balance Data:", balance_data)

        await asyncio.sleep(5)


async def main():
    data = MarketData()
    await initialize(data)
    await monitor_loop(data)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
