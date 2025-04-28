import asyncio
import os
import time
from dotenv import load_dotenv
import polars as pl

from krex.async_support.bybit.client import Client
from krex.websocket.bybit import BybitPublicWsClient, BybitPrivateWsClient
from krex.websocket.data.market_data import MarketData
from krex.websocket.bot.slack import Slack
from krex.utils.common_dataframe import to_dataframe

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

    bybit_client = Client(
        api_key=os.getenv("BYBIT_APIKEY"),
        api_secret=os.getenv("BYBIT_APISECRET"),
    )
    await bybit_client.async_init()

    raw = await bybit_client.get_kline(
        product_symbol="ETH-USDT-SWAP",
        interval="1m",
        startTime=int((time.time() - 60 * 100) * 1000),
        limit=100,
    )
    kline_list = raw.get("result", {}).get("list", [])
    kline_df = to_dataframe(
        kline_list, schema=["start", "open", "high", "low", "close", "volume", "turnover"]
    ).with_columns((pl.col("start").cast(pl.Int64) / 1000).cast(pl.Datetime).alias("datetime"))

    await shared_data.update_kline_data("bybit", "ETH-USDT-SWAP", kline_df)

    public_ws_client = await BybitPublicWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                "orderbook.1.ETHUSDT",
                "kline.1.ETHUSDT",
            ],
        },
        slack=slack,
        slack_bot_name="GHOST",
        slack_channel_name="CRITICAL",
    )
    public_ws_client.market_data = shared_data

    private_ws_client = await BybitPrivateWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                "order",
                "position",
                "wallet",
            ],
        },
        api_key=os.getenv("BYBIT_APIKEY"),
        api_secret=os.getenv("BYBIT_APISECRET"),
        slack=slack,
        slack_bot_name="GHOST",
        slack_channel_name="CRITICAL",
    )
    private_ws_client.market_data = shared_data

    asyncio.create_task(public_ws_client.start())
    asyncio.create_task(private_ws_client.start())

    return public_ws_client, private_ws_client


async def monitor_loop(shared_data: MarketData):
    while True:
        depth_data = await shared_data.get_all_depth_data()
        kline_data = await shared_data.get_all_kline_data()
        trade_data = await shared_data.get_all_trade_statuses()
        balance_data = await shared_data.get_all_balances()

        print("Depth Data:", depth_data)
        print("Kline Data:", kline_data)
        print("Trade Data:", trade_data)
        print("Balance Data:", balance_data)

        await asyncio.sleep(5)


async def main():
    shared_data = MarketData()
    await initialize(shared_data)
    await monitor_loop(shared_data)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
