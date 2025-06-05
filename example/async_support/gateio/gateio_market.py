import asyncio
import krex.async_support as krex


async def main():
    client = await krex.gateio()

    try:
        result = await client.get_all_futures_contracts()
        print(result)

        result = await client.get_a_single_futures_contract(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_contract_order_book(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_contract_kline(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_contract_list_tickers(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_futures_funding_rate_history(product_symbol="BTC-USDT-SWAP")
        print(result)

        result = await client.get_contract_order_book(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
        print(result)

        result = await client.get_contract_kline(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
        print(result)

        result = await client.get_contract_list_tickers(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
        print(result)

        result = await client.get_spot_all_currency_pairs()
        print(result)

        result = await client.get_spot_order_book(product_symbol="BTC-USDT-SPOT")
        print(result)

        result = await client.get_spot_kline(product_symbol="BTC-USDT-SPOT")
        print(result)

        result = await client.get_spot_list_tickers(product_symbol="BTC-USDT-SPOT")
        print(result)

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
