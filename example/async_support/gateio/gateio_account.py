import os
from dotenv import load_dotenv
import asyncio
import krex.async_support as krex

load_dotenv()


async def main():
    async with krex.gateio(
        api_key=os.getenv("GATEIO_APIKEY"),
        api_secret=os.getenv("GATEIO_APISECRET"),
    ) as client:
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


if __name__ == "__main__":
    asyncio.run(main())
