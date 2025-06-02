import asyncio
import krex.async_support as krex

BINANCE_APIKEY = "ovqxr2nXR50oeKo47CVKZTZ7ZmaCY3y1q7iAEOfsDXliAv52koJIcHEtlHDH30AU"
BINANCE_APISECRET = "sZ4nwX3owfZNDu4qBu0Y4H8zbic4E6FLtkbbNytV5Z6S77ZTiCgGxgYxHVitq4GQ"


async def main():
    async with krex.binance(
        api_key=BINANCE_APIKEY,
        api_secret=BINANCE_APISECRET,
    ) as client:
        result = await client.get_account_balance()
        print(result)

        result = await client.get_income_history()
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
