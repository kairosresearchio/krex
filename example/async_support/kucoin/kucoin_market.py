import asyncio
import krex.async_support as krex
import os
from dotenv import load_dotenv

load_dotenv()


KUCOIN_API_KEY = os.getenv("KUCOIN_API_KEY")
KUCOIN_API_SECRET = os.getenv("KUCOIN_API_SECRET")
KUCOIN_API_PASSPHRASE = os.getenv("KUCOIN_API_PASSPHRASE")


async def main():
    try:
        client = await krex.kucoin(
            api_key=KUCOIN_API_KEY,
            api_secret=KUCOIN_API_SECRET,
            passphrase=KUCOIN_API_PASSPHRASE,
        )
        # instrument_info = await client.get_spot_instrument_info()
        # print(instrument_info)

        # Test get_spot_ticker with BTC-USDT
        # ticker = await client.get_spot_ticker(product_symbol="BTC-USDT-SPOT")
        # print("BTC-USDT Ticker:")
        # print(ticker)

        # print("--------------------------------\n")

        # # Test get_spot_all_tickers
        # all_tickers = await client.get_spot_all_tickers()
        # print("All Tickers:")
        # print(all_tickers)

        # print("--------------------------------\n")

        # # Test get_spot_orderbook with BTC-USDT (sign = true)
        orderbook = await client.get_spot_orderbook(product_symbol="BTC-USDT-SPOT")
        print("BTC-USDT Orderbook:")
        print(orderbook)

        # print("--------------------------------\n")

        # Test get_spot_public_trades with BTC-USDT
        # public_trades = await client.get_spot_public_trades(product_symbol="BTC-USDT-SPOT")
        # print("BTC-USDT Public Trades:")
        # print(public_trades)

        # print("--------------------------------\n")

        # Test get_spot_kline with BTC-USDT
        # kline = await client.get_spot_kline(product_symbol="BTC-USDT-SPOT", type="1m")
        # print("BTC-USDT Kline (1hour):")
        # print(kline)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
