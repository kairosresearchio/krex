import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


BINGX_API_KEY = os.getenv("BINGX_API_KEY")
BINGX_API_SECRET = os.getenv("BINGX_API_SECRET")


async def main():
    client = await krex.bingx(
        api_key=BINGX_API_KEY,
        api_secret=BINGX_API_SECRET,
    )

    try:
        order_history = await client.get_order_history(product_symbol="BTC-USDT-SWAP", limit=10)
        print(order_history)

        open_orders = await client.get_open_orders()
        print(open_orders)

        close_swap_position = await client.close_swap_position(positionId="1937516840487182336")
        print(close_swap_position)

        order_detail = await client.get_order_detail(product_symbol="BTC-USDT-SWAP", orderId=1937513956622163968)
        print(order_detail)

        market_buy = await client.place_swap_market_buy_order(
            product_symbol="BTC-USDT-SWAP",
            quantity=0.0001,
        )
        print(market_buy)

        market_sell = await client.place_swap_market_sell_order(
            product_symbol="BTC-USDT-SWAP",
            quantity=0.0001,
        )
        print(market_sell)

        close_all_positions = await client.close_swap_all_positions(
            product_symbol="BTC-USDT-SWAP",
        )
        print(close_all_positions)

        limit_buy = await client.place_swap_limit_buy_order(
            product_symbol="BTC-USDT-SWAP",
            quantity=0.0001,
            price=105292,
        )
        print(limit_buy)

        limit_sell = await client.place_swap_limit_sell_order(
            product_symbol="BTC-USDT-SWAP",
            quantity=0.0001,
            price=200000,
        )
        print(limit_sell)

        post_only_buy = await client.place_swap_post_only_buy_order(
            product_symbol="BTC-USDT-SWAP",
            quantity=0.0001,
            price=60000,
        )
        print(post_only_buy)

        post_only_sell = await client.place_swap_post_only_sell_order(
            product_symbol="BTC-USDT-SWAP",
            quantity=0.0001,
            price=200000,
        )
        print(post_only_sell)

        place_batch_order = await client.place_swap_batch_order(
            batchOrders=[
                {
                    "symbol": "BTC-USDT",
                    "type": "MARKET",
                    "side": "BUY",
                    "positionSide": "LONG",
                    "quantity": 0.0001,
                }
            ]
        )
        print(place_batch_order)

        cancel_swap_order = await client.cancel_swap_order(product_symbol="BTC-USDT-SWAP", orderId=1937499540497326080)
        print(cancel_swap_order)

        cancel_swap_batch_order = await client.cancel_swap_batch_order(
            product_symbol="BTC-USDT-SWAP",
            orderIdList=[
                1937511261815398401,
                1937511262645870592,
            ],
        )
        print(cancel_swap_batch_order)

        cancel_swap_all_orders = await client.cancel_swap_all_orders(product_symbol="BTC-USDT-SWAP", type_="LIMIT")
        print(cancel_swap_all_orders)

        replace_swap_order = await client.replace_swap_order(
            product_symbol="BTC-USDT-SWAP",
            orderId="1937512049111425024",
            cancelOrderId=1937512049111425024,
            cancelReplaceMode="STOP_ON_FAILURE",
            type_="LIMIT",
            side="BUY",
            positionSide="LONG",
        )
        print(replace_swap_order)

        order_history = await client.get_order_history(product_symbol="BTC-USDT-SWAP", limit=10)
        print(order_history)

        change_margin_type = await client.change_margin_type(product_symbol="BTC-USDT-SWAP", marginType="CROSSED")
        print(change_margin_type)

        get_margin_type = await client.get_margin_type(product_symbol="BTC-USDT-SWAP")
        print(get_margin_type)

        set_leverage = await client.set_leverage(product_symbol="BTC-USDT-SWAP", side="SHORT", leverage=10)
        print(set_leverage)

        get_leverage = await client.get_leverage(product_symbol="BTC-USDT-SWAP")
        print(get_leverage)

        set_position_mode = await client.set_position_mode(dualSidePosition="true")
        print(set_position_mode)

        get_position_mode = await client.get_position_mode()
        print(get_position_mode)
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
