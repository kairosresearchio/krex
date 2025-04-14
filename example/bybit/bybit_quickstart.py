from krex.http.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"
TESTNET = False  # True means your API keys were generated on testnet.bybit.com

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)

fee_rates = client.get_fee_rates(product_symbol="BTC-USDT-SWAP")
print(fee_rates)
