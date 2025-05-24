import asyncio
from krex.async_support.bybit.client import Client


async def main():
    async with Client() as client:
        result = await client.get_instruments_info(category="spot")
        print(result)

        result = await client.get_kline(
            product_symbol="BTC-USDT-SPOT",
            interval="1m",
        )
        print(result)

        result = await client.get_orderbook(
            product_symbol="BTC-USDT-SPOT",
        )
        print(result)

        result = await client.get_tickers()
        print(result)

        result = await client.get_funding_rate_history(
            product_symbol="BTC-USDT-SWAP",
        )
        print(result)

        result = await client.get_public_trade_history(
            product_symbol="BTC-USDT-SPOT",
            limit=5,
        )
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
