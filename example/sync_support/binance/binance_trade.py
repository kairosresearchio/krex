from krex.binance.client import Client

BINANCE_APIKEY = "ovqxr2nXR50oeKo47CVKZTZ7ZmaCY3y1q7iAEOfsDXliAv52koJIcHEtlHDH30AU"
BINANCE_APISECRET = "sZ4nwX3owfZNDu4qBu0Y4H8zbic4E6FLtkbbNytV5Z6S77ZTiCgGxgYxHVitq4GQ"

client = Client(
    api_key=BINANCE_APIKEY,
    api_secret=BINANCE_APISECRET,
)

result = client.set_leverage(
    product_symbol="BTC-USDT-SWAP",
    leverage=3,
)
print(result)

result = client.place_future_market_buy_order(
    product_symbol="XRP-USDT-SWAP",
    quantity=5,
)
print(result)

result = client.place_future_market_sell_order(
    product_symbol="XRP-USDT-SWAP",
    quantity=5,
)
print(result)

result = client.place_future_limit_buy_order(
    product_symbol="XRP-USDT-SWAP",
    quantity=5,
    price="2.2768",
)
print(result)

result = client.place_future_limit_sell_order(
    product_symbol="XRP-USDT-SWAP",
    quantity=5,
    price="2.277",
)
print(result)

result = client.place_future_post_only_limit_buy_order(
    product_symbol="XRP-USDT-SWAP",
    quantity=5,
    price="2.26",
)
print(result)

result = client.place_future_post_only_limit_sell_order(
    product_symbol="XRP-USDT-SWAP",
    quantity=5,
    price="2.278",
)
print(result)

result = client.cancel_future_order(
    product_symbol="XRP-USDT-SWAP",
    orderId="100916566432",
)
print(result)

result = client.get_future_order(
    product_symbol="XRP-USDT-SWAP",
    orderId="100916566432",
)
print(result)

result = client.cancel_all_future_open_order(
    product_symbol="XRP-USDT-SWAP",
)
print(result)

result = client.get_future_all_order(
    product_symbol="XRP-USDT-SWAP",
)
print(result)

result = client.get_future_all_open_order(
    product_symbol="XRP-USDT-SWAP",
)
print(result)

result = client.get_future_open_order(
    product_symbol="XRP-USDT-SWAP",
    orderId="100917394683",
)
print(result)

result = client.get_future_position(
    product_symbol="XRP-USDT-SWAP",
)
print(result)
