import asyncio
from krex.async_support.hyperliquid.client import Client

async def main():
    async with Client(testnet= True) as client:
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
            interval= "1m",
            startTime= 1696128000000,
            )
        print(result)

        result = await client.funding_rate_history(
            product_symbol="BTC-USDC-SWAP",
            startTime=1696128000000
            )
        print(result)


if __name__ == "__main__":
    asyncio.run(main())