from krex.bybit.client import Client


client = Client()

result = client.get_instruments_info(category="spot")
print(result)

result = client.get_kline(
    product_symbol="BTC-USDT-SPOT",
    interval="1m",
)
print(result)

result = client.get_orderbook(
    product_symbol="BTC-USDT-SPOT",
)
print(result)

result = client.get_tickers()
print(result)

result = client.get_funding_rate_history(
    product_symbol="BTC-USDT-SWAP",
)
print(result)

result = client.get_public_trade_history(
    product_symbol="BTC-USDT-SWAP",
    limit=5,
)
print(result)
