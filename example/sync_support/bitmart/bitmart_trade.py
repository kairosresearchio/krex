import krex

BITMART_API_KEY = "613c8332848ff6b83aa915ae6270f2e842901036"
BITMART_API_SECRET = "66b82353bfee263185b36bdcaa244ee805c68aa87fd593addcd5124ff334ea3f"
MEMO = "trade"

client = krex.bitmart(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)

res = client.place_post_only_limit_buy_order(
    product_symbol="BTC-USDT-SPOT",
    size="0.0001",
    price="80000",
    client_order_id="test",
)
print("1. place_post_only_limit_buy_order:", res)

res = client.cancel_spot_order(
    product_symbol="BTC-USDT-SPOT",
    client_order_id="test",
)
print("2. cancel_spot_order:", res)

res = client.get_contract_position(
    product_symbol="BTC-USDT-SWAP",
)
print("3. get_contract_position:", res)
