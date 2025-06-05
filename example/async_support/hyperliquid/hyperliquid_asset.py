import asyncio
import krex.async_support as krex


async def main():
    wallet_address = ""
    client = await krex.hyperliquid()

    try:
        result = await client.user_vault_equities(user=wallet_address)
        print(result)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
