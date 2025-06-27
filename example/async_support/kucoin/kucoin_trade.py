import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv
import uuid

load_dotenv()

KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = os.getenv("KUCOIN_API_PASSPHRASE")

async def main():
    client = await krex.kucoin(
        api_key=KUCOIN_API_KEY,
        api_secret=KUCOIN_API_SECRET,
        passphrase=KUCOIN_API_PASSPHRASE,
    )

    try:
        # test place market buy order
        # result = await client.place_market_buy_order(
        #     product_symbol="BOME-USDT-SPOT",
        #     size="1000",
        # )
        # print("✅ Order placed successfully:")
        # print(result)

        # await asyncio.sleep(3)

        # await asyncio.sleep(3)

        # # test place market sell order
        # result = await client.place_market_sell_order(
        #     product_symbol="BOME-USDT-SPOT",
        #     size="1000",
        # )
        # print("✅ Order placed successfully:")
        # print(result)

        # test place limit buy order
        # result = await client.place_limit_buy_order(
        #     product_symbol="BOME-USDT-SPOT",
        #     size="1000",
        #     price="0.0013",
        # )
        # print("✅ Order placed successfully:")
        # print(result)

        # # test place limit sell order
        # result = await client.place_limit_sell_order(
        #     product_symbol="BOME-USDT-SPOT",
        #     size="1000",
        #     price="0.0015",
        # )
        # print("✅ Order placed successfully:")
        # print(result)

        # test place post only limit buy order
        # result = await client.place_post_only_limit_buy_order(
        #     product_symbol="BOME-USDT-SPOT",
        #     size="1000",
        #     price="0.0013",
        # )
        # print("✅ Order placed successfully:")

        
        # Test batch limit orders only
        # print("\nTesting batch limit orders...")
        # limit_orders = [
        #     {
        #         "symbol": "BOME-USDT-SPOT",
        #         "side": "buy",
        #         "size": "1000",
        #         "price": "0.0012",
        #     },
        #     {
        #         "symbol": "BOME-USDT-SPOT",
        #         "side": "sell",
        #         "size": "1000",
        #         "price": "0.0016",
        #     },
        #     {
        #         "symbol": "USDC-USDT-SPOT",
        #         "side": "buy",
        #         "size": "10",
        #         "price": "0.98",
        #     },
        # ]
        
        # result = await client.place_batch_limit_orders(limit_orders)
        # print("✅ Batch limit orders placed successfully:")
        # print(result)
        
        # await asyncio.sleep(10)
        
        # Test batch market orders only
        # print("\nTesting batch market orders...")
        # market_orders = [
        #     {
        #         "symbol": "BOME-USDT-SPOT",
        #         "side": "buy",
        #         "size": "300",
        #     },
        #     {
        #         "symbol": "BOME-USDT-SPOT",
        #         "side": "sell",
        #         "size": "300",
        #     }
        # ]
        
        # result = await client.place_batch_market_orders(market_orders)
        # print("✅ Batch market orders placed successfully:")
        # print(result)

        # # place limit buy order
        # result = await client.place_limit_buy_order(
        #     product_symbol="BOME-USDT-SPOT",
        #     size="1000",
        #     price="0.0013",
        # )
        # print("✅ Order placed successfully:")
        # print(result)

        # # get order id
        # if isinstance(result, dict) and "data" in result:
        #     order_id = result["data"]["orderId"]
        #     print(f"✅ Order ID: {order_id}")
            
        #     # wait 3 seconds
        #     await asyncio.sleep(3)

        #     # test cancel order
        #     cancel_result = await client.cancel_order(
        #         orderId=order_id,
        #         product_symbol="BOME-USDT-SPOT",
        #     )
        #     print("✅ Order cancelled successfully:")
        #     print(cancel_result)
        # else:
        #     print("❌ Could not extract order ID from response")

        # test cancel all orders by symbol
        # result = await client.cancel_all_orders_by_symbol(
        #     product_symbol="BOME-USDT-SPOT",
        # )
        # print("✅ All orders cancelled successfully:")
        # print(result)

        # Test cancel all orders (all symbols)
        # print("\nTesting cancel all orders (all symbols)...")
        # try:
        #     cancel_all_result = await client.cancel_all_orders()
        #     print("✅ Cancel all orders (all symbols) successful:")
        #     print(cancel_all_result)
            
        # except Exception as e:
        #     print(f"❌ Cancel all orders failed: {e}")


        # await asyncio.sleep(10)

        # test get open orders
        # result = await client.get_open_orders(
        #     product_symbol="BOME-USDT-SPOT",
        # )
        # print("✅ Open orders retrieved successfully:")
        # print(result)

        # test get trade history
        result = await client.get_trade_history(
            product_symbol="BOME-USDT-SPOT",
        )
        print("✅ Trade history retrieved successfully:")
        print(result)

    except Exception as e:
        print(f"❌ Test setup failed: {e}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())