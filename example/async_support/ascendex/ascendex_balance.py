import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


ASCENDEX_API_KEY = os.getenv("ASCENDEX_API_KEY")
ASCENDEX_API_SECRET = os.getenv("ASCENDEX_API_SECRET")


async def main():
    client = await krex.ascendex(
        api_key=ASCENDEX_API_KEY,
        api_secret=ASCENDEX_API_SECRET,
    )

    try:
        balance = await client.get_cash_account_balance()
        print(balance)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
