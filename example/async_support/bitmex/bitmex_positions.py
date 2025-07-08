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
        positions = await client.get_positions()
        print(positions)

        res = await client.switch_mode(product_symbol="XBT-USDT-SWAP", enabled=True)
        print(res)

        res = await client.set_leverage(product_symbol="XBT-USDT-SWAP", leverage=10, cross_margin=True)
        print(res)

        margining_mode = await client.set_margining_mode()
        print(margining_mode)

        margining_mode = await client.get_margining_mode()
        print(margining_mode)

        margin = await client.get_margin()
        print(margin)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
