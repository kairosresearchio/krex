import asyncio
import krex.async_support as krex


async def main():
    wallet_address = ""
    client = await krex.hyperliquid(testnet=True)

    try:
        result = await client.clearinghouse_state(user=wallet_address)
        print(result)

        result = await client.open_orders(user=wallet_address)
        print(result)

        result = await client.user_fills(user=wallet_address)
        print(result)

        result = await client.user_rate_limit(user=wallet_address)
        print(result)

        result = await client.order_status(user=wallet_address, oid=32755192478)
        print(result)

        result = await client.historical_orders(user=wallet_address)
        print(result)

        result = await client.subaccounts(user=wallet_address)
        print(result)

        result = await client.user_role(user=wallet_address)
        print(result)

        result = await client.portfolio(user=wallet_address)
        print(result)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
