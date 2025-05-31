from krex.hyperliquid.client import Client


client = Client()

result = client.meta()
print(result)

result = client.spot_meta()
print(result)

result = client.meta_and_asset_ctxs()
print(result)

result = client.spot_meta_and_asset_ctxs()
print(result)

result = client.l2book(product_symbol="BTC-USD-SWAP")
print(result)

result = client.candle_snapshot(
    product_symbol="BTC-USD-SWAP",
    interval= "1m",
    startTime= 1696128000000,
    )
print(result)

result = client.funding_rate_history(
    product_symbol="BTC-USD-SWAP",
    startTime=1696128000000)
print(result)





