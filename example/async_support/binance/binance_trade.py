import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


async def main():
    client = await krex.binance(
        api_key=BINANCE_API_KEY,
        api_secret=BINANCE_API_SECRET,
    )

    try:
        # place_spot_limit_buy_order
        result = await client.place_spot_limit_buy_order(
            product_symbol="USDC-USDT-SPOT",
            quantity=10,
            price=0.95,
        )
        print(result)

        await asyncio.sleep(5)

        # cancel_all_spot_orders
        result = await client.cancel_all_spot_orders(
            product_symbol="USDC-USDT-SPOT",
        )
        print(result)

        # place_spot_market_buy_order
        # result = await client.place_spot_market_buy_order(
        #     product_symbol="USDC-USDT-SPOT",
        #     quantity=10,
        # )
        # print(result)

        # place_spot_market_sell_order
        # result = await client.place_spot_market_sell_order(
        #     product_symbol="USDC-USDT-SPOT",
        #     quantity=10,
        # )
        # print(result)

        # result = await client.place_future_market_buy_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     quantity=5,
        # )
        # print(result)

        # result = await client.place_future_market_sell_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     quantity=5,
        # )
        # print(result)

        # result = await client.place_future_limit_buy_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     quantity=5,
        #     price="2.2768",
        # )
        # print(result)

        # result = await client.place_future_limit_sell_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     quantity=5,
        #     price="2.277",
        # )
        # print(result)

        # result = await client.place_future_post_only_limit_buy_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     quantity=5,
        #     price="2.26",
        # )
        # print(result)

        # result = await client.place_future_post_only_limit_sell_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     quantity=5,
        #     price="2.278",
        # )
        # print(result)

        # result = await client.cancel_future_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     orderId="100916566432",
        # )
        # print(result)

        # result = await client.get_future_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     orderId="100916566432",
        # )
        # print(result)

        # result = await client.cancel_all_future_open_order(
        #     product_symbol="XRP-USDT-SWAP",
        # )
        # print(result)

        # result = await client.get_future_all_order(
        #     product_symbol="XRP-USDT-SWAP",
        # )
        # print(result)

        # result = await client.get_future_all_open_order(
        #     product_symbol="XRP-USDT-SWAP",
        # )
        # print(result)

        # result = await client.get_future_open_order(
        #     product_symbol="XRP-USDT-SWAP",
        #     orderId="100917394683",
        # )
        # print(result)

        # result = await client.get_future_position(
        #     product_symbol="XRP-USDT-SWAP",
        # )
        # print(result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
