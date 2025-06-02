import asyncio
import krex.async_support as krex


async def main():
    async with krex.okx() as client:
        res = await client.get_public_instruments(instType="SPOT")
        print(res)

        res = await client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
        print(res)

        res = await client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
