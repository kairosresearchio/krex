import krex
import os
from dotenv import load_dotenv

load_dotenv()


BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


client = krex.binance(
    api_key=BINANCE_API_KEY,
    api_secret=BINANCE_API_SECRET,
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
