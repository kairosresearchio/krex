import os
from dotenv import load_dotenv
import asyncio
import krex.async_support as krex

load_dotenv()


async def main():
    client = await krex.gateio(
        api_key=os.getenv("GATEIO_API_KEY"),
        api_secret=os.getenv("GATEIO_API_SECRET"),
    )

    try:
        result = await client.get_futures_account()
        print(result)

        result = await client.get_futures_account_book()
        print(result)

        result = await client.get_delivery_account()
        print(result)

        result = await client.get_delivery_account_book()
        print(result)

        result = await client.get_spot_account(ccy="btc")
        print(result)

        result = await client.get_spot_account_book()
        print(result)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
