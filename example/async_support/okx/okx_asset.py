import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()

OKX_API_KEY = os.getenv("OKX_API_KEY")
OKX_API_SECRET = os.getenv("OKX_API_SECRET")
OKX_PASSPHRASE = os.getenv("OKX_PASSPHRASE")


async def main():
    client = await krex.okx(
        api_key=OKX_API_KEY,
        api_secret=OKX_API_SECRET,
        passphrase=OKX_PASSPHRASE,
    )

    try:
        res = await client.get_currencies()
        print(res)

        res = await client.get_balances()
        print(res)

        res = await client.get_asset_valuation()
        print(res)

        res = await client.get_bills()
        print(res)

        res = await client.get_deposit_address(ccy="BTC")
        print(res)

        res = await client.get_deposit_history()
        print(res)

        res = await client.get_bills()
        print(res)

        res = await client.get_withdrawal_history()
        print(res)

        res = await client.get_exchange_list()
        print(res)

        res = await client.post_monthly_statement(month="Mar")
        print(res)

        res = await client.get_monthly_statement(month="Mar")
        print(res)

        res = await client.get_convert_currencies()
        print(res)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
