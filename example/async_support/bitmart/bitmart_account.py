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
        res = await client.get_account_balance()
        print("1. get_account_balance:", "\n", res, "\n")

        res = await client.get_account_currencies()
        print("2. get_account_currencies:", "\n", res, "\n")

        res = await client.get_spot_wallet()
        print("3. get_spot_wallet:", "\n", res, "\n")

        res = await client.get_deposit_address(currency="BTC")
        print("4. get_deposit_address:", "\n", res, "\n")

        res = await client.get_withdraw_charge(currency="BTC")
        print("5. get_withdraw_charge:", "\n", res, "\n")

        res = await client.get_deposit_withdraw_history(currency="USDT")
        print("6. get_deposit_withdraw_history:", "\n", res, "\n")

        res = await client.get_deposit_withdraw_history_detail(id="26695771")
        print("7. get_deposit_withdraw_history_detail:", "\n", res, "\n")

        res = await client.get_contract_assets()
        print("8. get_contract_assets:", "\n", res, "\n")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
