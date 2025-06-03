import asyncio
import krex.async_support as krex

BINANCE_APIKEY = ""
BINANCE_APISECRET = ""


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
