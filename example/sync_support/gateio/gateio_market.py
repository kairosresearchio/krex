import os
from dotenv import load_dotenv
from krex.gateio.client import Client

load_dotenv()


client = Client(
    api_key=os.getenv("GATEIO_APIKEY"),
    api_secret=os.getenv("GATEIO_APISECRET"),
)

result = client.get_all_futures_contracts()
print(result)

result = client.get_a_single_futures_contract(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_contract_order_book(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_contract_kline(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_contract_list_tickers(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_futures_funding_rate_history(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_contract_order_book(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
print(result)

result = client.get_contract_kline(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
print(result)

result = client.get_contract_list_tickers(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
print(result)

result = client.get_spot_all_currency_pairs()
print(result)

result = client.get_spot_order_book(product_symbol="BTC-USDT-SPOT")
print(result)

result = client.get_spot_kline(product_symbol="BTC-USDT-SPOT")
print(result)

result = client.get_spot_list_tickers(product_symbol="BTC-USDT-SPOT")
print(result)
