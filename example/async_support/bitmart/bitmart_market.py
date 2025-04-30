import asyncio
from datetime import datetime, timedelta
from krex.async_support.bitmart.client import Client


async def main():
    async with Client() as client:
        # 1. get_spot_currencies
        res = await client.get_spot_currencies()
        print("1. get_spot_currencies:", "\n", res, "\n")

        # 2. get_trading_pairs
        res = await client.get_trading_pairs()
        print("2. get_trading_pairs:", "\n", res, "\n")

        # 3. get_trading_pairs_details
        res = await client.get_trading_pairs_details()
        print("3. get_trading_pairs_details:", "\n", res, "\n")

        # 4. get_ticker_of_all_pairs
        res = await client.get_ticker_of_all_pairs()
        print("4. get_ticker_of_all_pairs:", "\n", res, "\n")

        # 5. get_ticker_of_a_pair
        res = await client.get_ticker_of_a_pair(product_symbol="BTC-USDT-SPOT")
        print("5. get_ticker_of_a_pair:", "\n", res, "\n")

        # 6. get_spot_kline
        res = await client.get_spot_kline("BTC-USDT-SPOT", "5m")
        print("6. get_spot_kline:", "\n", res, "\n")

        # 7. get_depth
        res = await client.get_depth(product_symbol="BTC-USDT-SWAP")
        print("7. get_depth:", "\n", res, "\n")

        # 8. get_contract_kline
        res = await client.get_contract_kline(
            "BTC-USDT-SWAP",
            "5m",
            int((datetime.now() - timedelta(days=1)).timestamp()),
            int(datetime.now().timestamp()),
        )
        print("8. get_contract_kline:", "\n", res, "\n")


if __name__ == "__main__":
    asyncio.run(main())
