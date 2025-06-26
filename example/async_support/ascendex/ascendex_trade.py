import asyncio
import time
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


ASCENDEX_API_KEY = os.getenv("ASCENDEX_API_KEY")
ASCENDEX_API_SECRET = os.getenv("ASCENDEX_API_SECRET")


async def main():
    client = await krex.ascendex(
        api_key=ASCENDEX_API_KEY,
        api_secret=ASCENDEX_API_SECRET,
    )

    try:
        cancel_order = await client.cancel_spot_order(
            orderId="a197acaa3ea2U4884927732wDaPKyIct",
            product_symbol="BTC-USDT-SPOT",
        )
        print(cancel_order)

        orders = [
            {
                "id": "sampleRequestId1",
                "time": int(time.time() * 1000),
                "symbol": "BTC/USDT",
                "orderPrice": "34000",
                "orderQty": "0.0001",
                "orderType": "limit",
                "side": "buy",
            },
            {
                "id": "sampleRequestId2",
                "time": int(time.time() * 1000),
                "symbol": "BTC/USDT",
                "orderPrice": "35000",
                "orderQty": "0.0001",
                "orderType": "limit",
                "side": "buy",
            },
        ]
        place_orders = await client.place_spot_batch_orders(orders=orders)
        print(place_orders)

        orders_to_cancel = [
            {
                "orderId": "sampleRequestId1",
                "symbol": "BTC/USDT",
            },
            {
                "orderId": "sampleRequestId2",
                "symbol": "BTC/USDT",
            },
        ]
        cancel_orders = await client.cancel_spot_batch_orders(orders=orders_to_cancel)
        print(cancel_orders)

        # market_buy = await client.place_spot_market_buy_order(
        #     product_symbol="BTC-USDT-SPOT",
        #     orderQty="0.0001",
        # )
        # print(market_buy)

        # market_sell = await client.place_spot_market_sell_order(
        #     product_symbol="BTC-USDT-SPOT",
        #     orderQty="0.0001",
        # )
        # print(market_sell)

        # limit_buy = await client.place_spot_limit_buy_order(
        #     product_symbol="BTC-USDT-SPOT",
        #     orderQty="0.0001",
        #     orderPrice="60000",
        # )
        # print(limit_buy)

        # limit_sell = await client.place_spot_limit_sell_order(
        #     product_symbol="BTC-USDT-SPOT",
        #     orderQty="0.0001",
        #     orderPrice="120000",
        # )
        # print(limit_sell)

        # post_only_buy = await client.place_spot_post_only_buy_order(
        #     product_symbol="BTC-USDT-SPOT",
        #     orderQty="0.0001",
        #     orderPrice="60000",
        # )
        # print(post_only_buy)

        # post_only_sell = await client.place_spot_post_only_sell_order(
        #     product_symbol="BTC-USDT-SPOT",
        #     orderQty="0.0001",
        #     orderPrice="120000",
        # )
        # print(post_only_sell)

        # cancel_all_orders = await client.cancel_all_spot_orders(product_symbol="BTC-USDT-SPOT")
        # print(cancel_all_orders)

        # order_status = await client.get_order_status(orderId="1234567890")
        # print(order_status)

        # open_orders = await client.get_list_open_orders(product_symbol="BTC-USDT-SPOT")
        # print(open_orders)

        # account_info = await client.get_list_order_history(product_symbol="BTC-USDT-SPOT")
        # print(account_info)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
