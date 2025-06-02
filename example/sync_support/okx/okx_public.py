import krex


client = krex.okx()

result = client.get_public_instruments(instType="SPOT")
print(result)

result = client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
print(result)

result = client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
print(result)
