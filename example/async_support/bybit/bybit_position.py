import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")


async def main():
    client = await krex.bybit(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )

    try:
        result = await client.get_positions(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_closed_pnl()
        print(result)

        # result = await client.set_leverage(product_symbol="BTC-USDT-SWAP", leverage="10")
        # print(result)

        # result = await client.switch_position_mode(0, "BTCUSDT")
        # print(result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
