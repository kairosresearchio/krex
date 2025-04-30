import asyncio
from krex.async_support.okx.client import Client


async def main():
    async with Client() as client:
        res = await client.get_candles_ticks(product_symbol="BTC-USDT-SPOT")
        print(res)

        res = await client.get_orderbook(product_symbol="BTC-USDT-SPOT")
        print(res)

        res = await client.get_tickers(instType="SPOT")
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
