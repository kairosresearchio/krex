from krex.binance.client import Client


client = Client()

result = client.get_spot_exchange_info(product_symbol="BTC-USDT-SPOT")
print(result)

result = client.get_futures_exchange_info()
print(result)

result = client.get_futures_ticker(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_futures_kline(product_symbol="BTC-USDT-SWAP", interval="1m")
print(result)

result = client.get_futures_premium_index(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_futures_funding_rate(product_symbol="BTC-USDT-SWAP")
print(result)
