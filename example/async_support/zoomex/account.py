import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()

ZOOMEX_API_KEY = os.getenv("ZOOMEX_API_KEY")
ZOOMEX_API_SECRET = os.getenv("ZOOMEX_API_SECRET")


async def main():
    client = await krex.zoomex(api_key = ZOOMEX_API_KEY, api_secret = ZOOMEX_API_SECRET)

    res = await client.get_wallet_balance()
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
