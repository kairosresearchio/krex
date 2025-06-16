import krex
import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

client = krex.bybit(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=True,
)

result = client.get_open_orders(category="spot")
print(result)

result = client.get_order_history()
print(result)

result = client.get_execution_list()
print(result)

result = client.get_borrow_quota(product_symbol="BTC-USDT-SWAP", side="Buy")
print(result)

result = client.get_vip_margin_data()
print(result)

result = client.get_collateral()
print(result)

result = client.get_historical_interest_rate(currency="USDT")
print(result)

result = client.get_status_and_leverage()
print(result)

# result = client.place_limit_buy_order(
#     product_symbol="BTC-USDT-SWAP",
#     qty="0.001",
#     price="80000",
# )
# print(result)

# result = client.cancel_batch_orders(
#     request=[
#         {
#             "symbol": "BTCUSDT",
#             "orderId": "85bb8a3f-a59d-4e2a-ac3c-9d94a8ed7f2f",
#         },
#         {
#             "symbol": "BTCUSDT",
#             "orderId": "46c0a057-5208-4ec3-8023-a6b0bef86ee3",
#         },
#     ],
# )
# print(result)
