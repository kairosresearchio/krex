import asyncio
from krex.async_support.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"


async def main():
    async with Client(
        api_key=OKX_API_KEY,
        api_secret=OKX_API_SECRET,
        passphrase=OKX_PASSPHRASE,
    ) as client:
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


if __name__ == "__main__":
    asyncio.run(main())
