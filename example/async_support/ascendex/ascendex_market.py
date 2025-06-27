import asyncio
import krex.async_support as krex


async def main():
    client = await krex.ascendex()

    try:
        instrument_info = await client.get_spot_instrument_info()
        print(instrument_info)

        ticker = await client.get_spot_ticker(product_symbol="BTC-USDT-SPOT")
        print(ticker)

        kline = await client.get_spot_kline(product_symbol="BTC-USDT-SPOT", interval="1m")
        print(kline)

        orderbook = await client.get_spot_orderbook(product_symbol="BTC-USDT-SPOT")
        print(orderbook)

        public_trade = await client.get_spot_public_trade(product_symbol="BTC-USDT-SPOT")
        print(public_trade)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
