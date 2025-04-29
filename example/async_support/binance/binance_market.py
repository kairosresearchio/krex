import asyncio
from krex.async_support.binance.client import Client

BINANCE_APIKEY = "ovqxr2nXR50oeKo47CVKZTZ7ZmaCY3y1q7iAEOfsDXliAv52koJIcHEtlHDH30AU"
BINANCE_APISECRET = "sZ4nwX3owfZNDu4qBu0Y4H8zbic4E6FLtkbbNytV5Z6S77ZTiCgGxgYxHVitq4GQ"


async def main():
    async with Client(
        api_key=BINANCE_APIKEY,
        api_secret=BINANCE_APISECRET,
    ) as client:
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
