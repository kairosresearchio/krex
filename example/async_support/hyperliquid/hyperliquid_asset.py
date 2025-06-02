import asyncio
import krex.async_support as krex


async def main():
    wallet_address = ""
    async with krex.hyperliquid() as client:
        result = await client.user_vault_equities(user=wallet_address)
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
