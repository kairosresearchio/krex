import asyncio
import krex.async_support as krex

BINANCE_APIKEY = ""
BINANCE_APISECRET = ""


async def main():
    client = await krex.binance(
        api_key=BINANCE_APIKEY,
        api_secret=BINANCE_APISECRET,
    )

    try:
        result = await client.get_account_balance()
        print(result)

        result = await client.get_income_history()
        print(result)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
