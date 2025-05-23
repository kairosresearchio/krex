import asyncio
import os
from dotenv import load_dotenv

from krex.websocket.bybit import (
    BybitPublicSpotWsClient,
    BybitPublicLinearWsClient,
    BybitPrivateWsClient,
)
from krex.websocket.data.market_data import MarketData
# from krex.websocket.bot.slack import Slack

load_dotenv()


async def initialize(shared_data: MarketData):
    # slack = Slack(
    #     bot_tokens={
    #         "GHOST": os.getenv("SLACK_BOT_GHOST"),
    #     },
    #     channel_ids={
    #         "CRITICAL": os.getenv("SLACK_CHANNEL_CRITICAL"),
    #         "ALL_KAIROS": os.getenv("SLACK_CHANNEL_ALL_KAIROS"),
    #     },
    # )

    # Spot WebSocket
    public_spot_ws_client = await BybitPublicSpotWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                "orderbook.1.BTCUSDT",
            ],
        },
        is_sandbox=True,
    )
    public_spot_ws_client.market_data = shared_data

    # Linear WebSocket
    public_linear_ws_client = await BybitPublicLinearWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                "orderbook.1.BTCUSDT",
            ],
        },
        is_sandbox=True,
    )
    public_linear_ws_client.market_data = shared_data

    # Private WebSocket
    private_ws_client = await BybitPrivateWsClient.create(
        subscription={
            "op": "subscribe",
            "args": [
                "order",
                "wallet",
            ],
        },
        # slack=slack,
        # slack_bot_name="GHOST",
        # slack_channel_name="CRITICAL",
        api_key=os.getenv("BYBIT_APIKEY"),
        api_secret=os.getenv("BYBIT_APISECRET"),
        is_sandbox=True,
    )
    private_ws_client.market_data = shared_data

    # Start tasks
    # asyncio.create_task(public_spot_ws_client.start())
    asyncio.create_task(public_linear_ws_client.start())
    asyncio.create_task(private_ws_client.start())

    # return public_spot_ws_client, private_ws_client
    return public_linear_ws_client, private_ws_client


async def monitor_loop(shared_data: MarketData):
    while True:
        depth_data = await shared_data.get_all_depth_data()
        print(f"📊 Depth Data: {depth_data}")
        kline_data = await shared_data.get_all_kline_data()
        trade_data = await shared_data.get_all_trade_statuses()
        balance_data = await shared_data.get_all_balances()

        print("\n" + "=" * 40)

        # Display best bid and ask
        for source, ticker_map in depth_data.items():
            for symbol, ticker in ticker_map.items():
                if hasattr(ticker, "best_bid_price"):
                    print(f"📈 [{source}] {symbol} Best Bid: {ticker.best_bid_price} | Ask: {ticker.best_ask_price}")

        # Display latest klines
        for source, kline_map in kline_data.items():
            for symbol, df in kline_map.items():
                latest = df[-1] if len(df) > 0 else None
                if latest is not None:
                    print(f"🕒 [{source}] {symbol} Latest Kline Time: {latest['datetime']}, Close: {latest['close']}")

        # Display trade status
        for exchange, symbol_map in trade_data.items():
            for symbol, trade in symbol_map.items():
                print(
                    f"📋 [Trade] {symbol} Status: {trade.status.value} | Price: {trade.price} | Filled: {trade.filled_quantity}/{trade.quantity}"
                )

        # Display wallet balances
        for exchange, assets in balance_data.items():
            print(f"💰 [Balance] Exchange: {exchange.value}")
            for asset, balance in assets.items():
                print(f"    - {asset}: Available {balance.available_balance} | Frozen {balance.frozen_balance}")

        await asyncio.sleep(3)


async def main():
    shared_data = MarketData()
    await initialize(shared_data)
    await monitor_loop(shared_data)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
