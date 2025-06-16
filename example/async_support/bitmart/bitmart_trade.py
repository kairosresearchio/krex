import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()

BITMART_API_KEY = os.getenv("BITMART_API_KEY")
BITMART_API_SECRET = os.getenv("BITMART_API_SECRET")
MEMO = os.getenv("BITMART_MEMO")


async def main():
    client = await krex.bitmart(
        api_key=BITMART_API_KEY,
        api_secret=BITMART_API_SECRET,
        memo=MEMO,
    )

    try:
        res = await client.place_spot_post_only_limit_order(
            product_symbol="BTC-USDT-SPOT",
            size="0.0001",
            price="80000",
            client_order_id="test",
        )
        print("1. place_spot_post_only_limit_order:", res)

        res = await client.cancel_spot_order(
            product_symbol="BTC-USDT-SPOT",
            client_order_id="test",
        )
        print("2. cancel_spot_order:", res)

        res = await client.get_contract_position(
            product_symbol="BTC-USDT-SWAP",
        )
        print("3. get_contract_position:", res)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
