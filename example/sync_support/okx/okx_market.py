import krex


client = krex.okx()

result = client.get_candles_ticks(product_symbol="BTC-USDT-SPOT")
print(result)

result = client.get_orderbook(product_symbol="BTC-USDT-SPOT")
print(result)

result = client.get_tickers(instType="SPOT")
print(result)
