import asyncio
import krex.async_support as krex

BYBIT_API_KEY = ""
BYBIT_API_SECRET = ""


async def main():
    client = await krex.bybit(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    )

    try:
        result = await client.get_open_orders(category="spot")
        print(result)

        result = await client.get_order_history()
        print(result)

        result = await client.get_execution_list()
        print(result)

        result = await client.get_borrow_quota(product_symbol="BTC-USDT-SWAP", side="Buy")
        print(result)

        result = await client.get_vip_margin_data()
        print(result)

        result = await client.get_collateral()
        print(result)

        result = await client.get_historical_interest_rate(currency="USDT")
        print(result)

        result = await client.get_status_and_leverage()
        print(result)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
