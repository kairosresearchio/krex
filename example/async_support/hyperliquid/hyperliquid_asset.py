import asyncio
from krex.async_support.hyperliquid.client import Client

async def main():
    wallet_address = ""
    async with Client() as client:
        result = await client.user_vault_equities(
            user= wallet_address
        )
        print(result)

if __name__ == "__main__":
    asyncio.run(main())