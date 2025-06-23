import asyncio
from krex.async_support.ascendex import Client


async def main():
    """
    Example demonstrating AscendEX account operations with dynamic endpoint resolution
    """
    
    # Initialize client with API credentials
    client = Client(
        api_key="your_api_key",
        api_secret="your_api_secret",
        testnet=False  # Set to True for testnet
    )
    
    try:
        async with client:
            # This uses a static endpoint (/api/pro/v1/info)
            print("Getting account info...")
            account_info = await client.get_account_info()
            print(f"Account info: {account_info}")
            
            # This uses a dynamic endpoint ({ACCOUNT_GROUP}/api/pro/v1/cash/balance)
            # The {ACCOUNT_GROUP} will be automatically resolved from the account info
            print("\nGetting cash balance...")
            cash_balance = await client.get_cash_balance()
            print(f"Cash balance: {cash_balance}")
            
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main()) 