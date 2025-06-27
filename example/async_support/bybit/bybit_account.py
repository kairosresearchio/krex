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
        result = await client.get_wallet_balance()
        print(result)

        result = await client.get_transferable_amount(coins=["BTC", "ETH"])
        print(result)

        # result = await client.upgrade_to_unified_trading_account()
        # print(result)

        result = await client.get_borrow_history()
        print(result)

        result = await client.get_collateral_info()
        print(result)

        result = await client.get_fee_rates()
        print(result)

        result = await client.get_account_info()
        print(result)

        result = await client.get_transaction_log()
        print(result)

        # result = await client.set_collateral_coin("BTC", "ON")
        # print(result)

        # result = await client.set_margin_mode("PORTFOLIO_MARGIN")
        # print(result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
