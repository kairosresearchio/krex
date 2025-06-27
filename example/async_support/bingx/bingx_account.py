import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


BINGX_API_KEY = os.getenv("BINGX_API_KEY")
BINGX_API_SECRET = os.getenv("BINGX_API_SECRET")


async def main():
    client = await krex.bingx(
        api_key=BINGX_API_KEY,
        api_secret=BINGX_API_SECRET,
    )

    try:
        balance = await client.get_account_balance()
        print(balance)

        positions = await client.get_open_positions(product_symbol="BTC-USDT-SWAP")
        print(positions)

        fund_flow = await client.get_fund_flow(limit=5)
        print(fund_flow)

        listen_key = await client.get_listen_key()
        print(listen_key)

        if listen_key:
            keep_alive_response = await client.keep_alive_listen_key(listen_key)
            print(keep_alive_response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
