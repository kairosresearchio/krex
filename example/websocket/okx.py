import asyncio
import os
from dotenv import load_dotenv
import polars as pl

from krex.async_support.okx.client import Client
from krex.websocket.okx import OkxPublicWsClient, OkxPrivateWsClient
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

    symbol = "ETH-USDT-SWAP"

    okx_client = Client(
        api_key=os.getenv("OKX_APIKEY"),
        api_secret=os.getenv("OKX_APISECRET"),
        passphrase=os.getenv("OKX_PASSPHRASE"),
    )
    await okx_client.async_init()

    raw = await okx_client.get_candles_ticks(
        product_symbol=symbol,
        bar="1m",
        limit="100",
    )
    kline_data = raw.get("data", [])

    kline_df = to_dataframe(
        kline_data,
        schema=["ts", "o", "h", "l", "c", "vol", "volCcy", "volCcyQuote", "confirm"],
    ).rename(
        {
            "ts": "datetime",
            "o": "open",
            "h": "high",
            "l": "low",
            "c": "close",
            "vol": "volume",
        }
    )

    kline_df = kline_df.with_columns(
        [
            kline_df["datetime"].cast(pl.Int64).cast(pl.Datetime("ms")),
            kline_df["open"].cast(pl.Float64),
            kline_df["high"].cast(pl.Float64),
            kline_df["low"].cast(pl.Float64),
            kline_df["close"].cast(pl.Float64),
            kline_df["volume"].cast(pl.Float64),
        ]
    )

    await shared_data.update_kline_data("okx", symbol, kline_df)

    public_ws_client = await OkxPublicWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                {"channel": "bbo-tbt", "instId": symbol},
                {"channel": "candle1m", "instId": symbol},
            ],
        },
        slack=slack,
        slack_bot_name="GHOST",
        slack_channel_name="CRITICAL",
    )
    public_ws_client.market_data = shared_data

    private_ws_client = await OkxPrivateWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                {"channel": "orders", "instType": "SWAP"},
                {"channel": "account"},
                {"channel": "positions", "instType": "SWAP"},
            ],
        },
        api_key=os.getenv("OKX_APIKEY"),
        api_secret=os.getenv("OKX_APISECRET"),
        passphrase=os.getenv("OKX_PASSPHRASE"),
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
