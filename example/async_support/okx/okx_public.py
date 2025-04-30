import asyncio
from krex.async_support.okx.client import Client


async def main():
    async with Client() as client:
        res = await client.get_public_instruments(instType="SPOT")
        print(res)

        res = await client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
        print(res)

        res = await client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
