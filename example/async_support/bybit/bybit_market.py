import asyncio
import krex.async_support as krex


async def main():
    client = await krex.bybit()

    try:
        result = await client.get_instruments_info(cursor="first%3D1000000BABYDOGEUSDT%26last%3DSPECUSDT")
        print(result)

        # result = await client.get_kline(
        #     product_symbol="BTC-USDT-SPOT",
        #     interval="1m",
        # )
        # print(result)

        # result = await client.get_orderbook(
        #     product_symbol="BTC-USDT-SPOT",
        # )
        # print(result)

        # result = await client.get_tickers()
        # print(result)

        # result = await client.get_funding_rate_history(
        #     product_symbol="BTC-USDT-SWAP",
        # )
        # print(result)

        # result = await client.get_public_trade_history(
        #     product_symbol="BTC-USDT-SPOT",
        #     limit=5,
        # )
        # print(result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
