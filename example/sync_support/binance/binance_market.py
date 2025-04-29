from krex.binance.client import Client

BINANCE_APIKEY = "ovqxr2nXR50oeKo47CVKZTZ7ZmaCY3y1q7iAEOfsDXliAv52koJIcHEtlHDH30AU"
BINANCE_APISECRET = "sZ4nwX3owfZNDu4qBu0Y4H8zbic4E6FLtkbbNytV5Z6S77ZTiCgGxgYxHVitq4GQ"

client = Client(
    api_key=BINANCE_APIKEY,
    api_secret=BINANCE_APISECRET,
)

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
