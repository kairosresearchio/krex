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
        res = await client.get_order_list(
            product_symbol="BTC-USDT-SPOT",
        )
        print(res)

        res = await client.get_orders_history(
            instType="SPOT",
        )
        print(res)

        res = await client.get_orders_history_archive(
            instType="SPOT",
        )
        print(res)

        res = await client.get_fills()
        print(res)

        res = await client.get_fills_history(
            instType="SPOT",
        )
        print(res)

        res = await client.get_account_rate_limit()
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
