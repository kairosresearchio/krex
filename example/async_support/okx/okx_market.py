import asyncio
import krex.async_support as krex


async def main():
    async with krex.okx() as client:
        res = await client.get_candles_ticks(product_symbol="BTC-USDT-SPOT")
        print(res)

        res = await client.get_orderbook(product_symbol="BTC-USDT-SPOT")
        print(res)

        res = await client.get_tickers(instType="SPOT")
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
