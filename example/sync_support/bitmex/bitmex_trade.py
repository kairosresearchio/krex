import krex
import os
from dotenv import load_dotenv

load_dotenv()

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")


client = krex.bitmex(
    api_key=BITMEX_API_KEY,
    api_secret=BITMEX_API_SECRET,
)

order = client.place_market_buy_order(
    product_symbol="XRP-USDT-SPOT",
    orderQty=1000000,  # 1000000 XRP = 2 USDT
)
print(order)

order = client.place_market_buy_order(
    product_symbol="HYPE-USDT-SWAP",
    orderQty=10,
)
print(order)

order = client.place_market_sell_order(
    product_symbol="HYPE-USDT-SWAP",
    orderQty=10,
)
print(order)

order = client.place_limit_buy_order(
    product_symbol="HYPE-USDT-SWAP",
    orderQty=10,
    price=38,
)
print(order)

order = client.place_limit_sell_order(
    product_symbol="HYPE-USDT-SWAP",
    orderQty=10,
    price=38,
)
print(order)

order = client.place_post_only_buy_order(
    product_symbol="HYPE-USDT-SWAP",
    orderQty=10,
    price=37,
)
print(order)

order = client.place_post_only_sell_order(
    product_symbol="HYPE-USDT-SWAP",
    orderQty=10,
    price=38,
)
print(order)

order = client.amend_order(
    orderID="fb83b63d-15b8-46bd-b8df-81192bab82ee",
    price=37,
)
print(order)

order = client.cancel_order(
    orderID="f228d218-c95d-455f-bbaa-6fc108c1d1d5",
)
print(order)

order = client.cancel_all_orders(
    product_symbol="HYPE-USDT-SWAP",
)
print(order)

order = client.get_order(
    product_symbol="HYPE-USDT-SWAP",
)
print(order)
