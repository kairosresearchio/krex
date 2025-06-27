import asyncio
from krex.async_support import bingx


async def main():
    client = await bingx()

    try:
        instrument_info = await client.get_swap_instrument_info()
        print(instrument_info["data"][0])

        orderbook = await client.get_orderbook("BTC-USDT-SWAP", limit=10)
        print(orderbook)

        trades = await client.get_public_trades("BTC-USDT-SWAP", limit=5)
        print(trades["data"][0])

        klines = await client.get_kline("BTC-USDT-SWAP", "1h", limit=5)
        print(klines)

        ticker = await client.get_ticker("BTC-USDT-SWAP")
        print(ticker)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
