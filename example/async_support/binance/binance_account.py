import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


async def main():
    client = await krex.binance(
        api_key=BINANCE_API_KEY,
        api_secret=BINANCE_API_SECRET,
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
