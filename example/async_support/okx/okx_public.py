import asyncio
import krex.async_support as krex


async def main():
    client = await krex.okx()

    try:
        res = await client.get_public_instruments(instType="SPOT")
        print(res)

        res = await client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
        print(res)

        res = await client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
        print(res)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
