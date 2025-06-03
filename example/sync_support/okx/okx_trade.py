import krex

OKX_API_KEY = ""
OKX_API_SECRET = ""
OKX_PASSPHRASE = ""

client = krex.okx(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
)

result = client.get_order_list(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_orders_history(
    instType="SPOT",
)
print(result)

result = client.get_orders_history_archive(
    instType="SPOT",
)
print(result)

result = client.get_fills()
print(result)

result = client.get_fills_history(
    instType="SPOT",
)
print(result)

result = client.get_account_rate_limit()
print(result)
