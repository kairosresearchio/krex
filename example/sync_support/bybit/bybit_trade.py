from krex.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

result = client.get_open_orders(category="spot")
print(result)

result = client.get_order_history()
print(result)

result = client.get_execution_list()
print(result)

result = client.get_borrow_quota(product_symbol="BTC-USDT-SWAP", side="Buy")
print(result)

result = client.get_vip_margin_data()
print(result)

result = client.get_collateral()
print(result)

result = client.get_historical_interest_rate(currency="USDT")
print(result)

result = client.get_status_and_leverage()
print(result)
