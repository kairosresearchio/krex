import asyncio
import krex.async_support as krex

BYBIT_API_KEY = ""
BYBIT_API_SECRET = ""


async def main():
    async with krex.bybit(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    ) as client:
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


if __name__ == "__main__":
    asyncio.run(main())
