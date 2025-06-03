import krex

BYBIT_API_KEY = ""
BYBIT_API_SECRET = ""

client = krex.bybit(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

result = client.get_positions(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_closed_pnl()
print(result)

# result = client.set_leverage(product_symbol="BTC-USDT-SWAP", leverage="10")
# print(result)

# result = client.switch_position_mode(0, "BTCUSDT")
# print(result)
