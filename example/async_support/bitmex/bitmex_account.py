import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")


async def main():
    client = await krex.bitmex(
        api_key=BITMEX_API_KEY,
        api_secret=BITMEX_API_SECRET,
    )

    try:
        wallet_summary = await client.get_wallet_summary()
        for record in wallet_summary:
            scaled_amount = record["amount"] / 1000000
            scaled_deposited = record["deposited"] / 1000000

            print(f"Currency: {record['currency']}")
            print(f"Current Balance: {scaled_amount}")
            print(f"Total Deposit: {scaled_deposited}")
            print("---")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
