import asyncio
from krex.async_support.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"


async def main():
    async with Client(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    ) as client:
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


if __name__ == "__main__":
    asyncio.run(main())
