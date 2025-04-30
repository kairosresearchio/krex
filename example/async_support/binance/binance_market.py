import asyncio
from krex.async_support.binance.client import Client


async def main():
    async with Client() as client:
        result = await client.get_spot_exchange_info(product_symbol="BTC-USDT-SPOT")
        print(result)

        result = await client.get_futures_exchange_info()
        print(result)

        result = await client.get_futures_ticker(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_futures_kline(product_symbol="BTC-USDT-SWAP", interval="1m")
        print(result)

        result = await client.get_futures_premium_index(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_futures_funding_rate(product_symbol="BTC-USDT-SWAP")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
