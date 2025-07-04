from dotenv import load_dotenv
import krex

load_dotenv()


client = krex.gateio()

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
