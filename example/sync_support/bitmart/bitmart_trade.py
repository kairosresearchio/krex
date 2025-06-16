import krex
import os
from dotenv import load_dotenv

load_dotenv()

BITMART_API_KEY = os.getenv("BITMART_API_KEY")
BITMART_API_SECRET = os.getenv("BITMART_API_SECRET")
MEMO = os.getenv("BITMART_MEMO")


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
