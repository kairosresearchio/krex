from krex.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

result = client.get_positions()
print(result)

result = client.get_closed_pnl()
print(result)

# result = client.set_leverage(product_symbol="BTC-USDT-SWAP", leverage="10")
# print(result)

# result = client.switch_position_mode(0, "BTCUSDT")
# print(result)
