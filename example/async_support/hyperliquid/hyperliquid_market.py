import asyncio
import krex.async_support as krex


async def main():
    client = await krex.hyperliquid(testnet=True)

    try:
        result = await client.meta()
        print(result)

        result = await client.spot_meta()
        print(result)

        result = await client.meta_and_asset_ctxs()
        print(result)

        result = await client.spot_meta_and_asset_ctxs()
        print(result)

        result = await client.l2book(product_symbol="FLASK-USDC-SPOT")
        print(result)

        result = await client.candle_snapshot(
            product_symbol="BTC-USDC-SWAP",
            interval="1m",
            startTime=1696128000000,
        )
        print(result)

        result = await client.funding_rate_history(product_symbol="BTC-USDC-SWAP", startTime=1696128000000)
        print(result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
