import asyncio
from krex.async_support.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"


async def main():
    async with Client(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    ) as client:
        result = await client.get_coin_info()
        print(result)

        # result = await client.get_sub_uid()
        # print(result)

        result = await client.get_spot_asset_info()
        print(result)

        result = await client.get_coins_balance(accountType="FUND")
        print(result)

        result = await client.get_coin_balance(accountType="FUND", coin="BTC")
        print(result)

        result = await client.get_withdrawable_amount(coin="USDT")
        print(result)

        result = await client.get_internal_transfer_records()
        print(result)

        result = await client.get_universal_transfer_records()
        print(result)

        result = await client.get_deposit_records()
        print(result)

        result = await client.get_internal_deposit_records()
        print(result)

        # result = await client.get_master_deposit_addresults(coin="USDT")
        # print(result)

        result = await client.get_withdrawal_records()
        print(result)

        # result = await client.get_transferable_coin(
        #     fromAccountType="FUND",
        #     toAccountType="UNIFIED",
        # )
        # print(result)

        # result = await client.create_internal_transfer(
        #     coin="USDT",
        #     amount="1",
        #     fromAccountType="UNIFIED",
        #     toAccountType="FUND",
        # )
        # print(result)


if __name__ == "__main__":
    asyncio.run(main())
