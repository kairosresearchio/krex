import os
from dotenv import load_dotenv
import krex

load_dotenv()


client = krex.gateio(
    api_key=os.getenv("GATEIO_API_KEY"),
    api_secret=os.getenv("GATEIO_API_SECRET"),
)

# all done
# # ========== Futures ==========
# result = client.update_futures_positions_leverage(
#     product_symbol="BTC-USDT-SWAP",
#     leverage="3",
# )
# print(result)

# result = client.future_dual_mode_switch(dual_mode=False)
# print(result)

# # short
# result = client.place_contract_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=-1,
#     price="95000",
#     tif="gtc",
# )
# print(result)

# # long
# result = client.place_contract_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
#     price="0",
#     tif="ioc",
# )
# print(result)

# close
# result = client.place_contract_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=0,
#     price="0",
#     tif="ioc",
#     close=True,
# )
# print(result)

# result = client.place_contract_market_buy_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
# )
# print(result)

# result = client.place_contract_market_sell_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
# )
# print(result)

# result = client.place_contract_limit_buy_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
#     price="90000",
# )
# print(result)

# result = client.place_contract_limit_sell_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
#     price="100000",
# )
# print(result)

# result = client.place_contract_post_only_limit_buy_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
#     price="90000",
# )
# print(result)

# result = client.place_contract_post_only_limit_sell_order(
#     product_symbol="BTC-USDT-SWAP",
#     size=1,
#     price="100000",
# )
# print(result)

# result = client.cancel_contract_all_order_matched(
#     product_symbol="BTC-USDT-SWAP",
# )
# print(result)

# result = client.get_futures_all_positions()
# print(result)

# result = client.get_contract_single_positions(product_symbol="BTC-USDT-SWAP")
# print(result)

# orders = [
#     {
#         "product_symbol": "BTC-USDT-SWAP",
#         "size": 1,
#         "price": "60000",
#         "tif": "gtc",
#     },
#     {
#         "product_symbol": "ETH-USDT-SWAP",
#         "size": -2,
#         "price": "3000",
#         "tif": "gtc",
#     },
# ]

# result = client.place_futures_batch_order(orders, ccy="usdt")
# print(result)

# result = client.get_contract_order_list(status="open")
# print(result)

# result = client.get_contract_single_order(order_id="36028800562142587")
# print(result)

# result = client.cancel_contract_single_order(order_id="36028800562142587")
# print(result)

# result = client.amend_futures_single_order(
#     order_id="36028800562493938",
#     price="91000",
# )
# print(result)

# result = client.get_trading_history(product_symbol="BTC-USDT-SWAP")
# print(result)

# result = client.get_futures_position_close_history(
#     product_symbol="BTC-USDT-SWAP",
# )
# print(result)

# # ========== Delivery ==========
# result = client.place_contract_post_only_limit_buy_order(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     size=1,
#     price="90000",
#     path="delivery",
# )
# print(result)

# result = client.place_contract_post_only_limit_sell_order(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     size=1,
#     price="100000",
#     path="delivery",
# )
# print(result)

# result = client.get_contract_single_positions(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     path="delivery",
# )
# print(result)

# result = client.get_contract_order_list(status="open", path="delivery")
# print(result)

# result = client.cancel_contract_all_order_matched(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     path="delivery",
# )
# print(result)

# result = client.get_contract_single_order(
#     order_id="9803771016",
#     path="delivery",
# )
# print(result)

# result = client.cancel_contract_single_order(
#     order_id="9803771016",
#     path="delivery",
# )
# print(result)

# result = client.place_contract_order(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     size=1,
#     price="0",
#     tif="ioc",
#     path="delivery",
# )
# print(result)

# result = client.get_trading_history(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     path="delivery",
# )
# print(result)

# result = client.get_delivery_all_positions()
# print(result)

# result = client.update_delivery_positions_leverage(
#     product_symbol="BTC-USDT-20250502-SWAP",
#     leverage="3",
# )
# print(result)

# result = client.get_delivery_position_close_history(
#     product_symbol="BTC-USDT-20250502-SWAP",
# )
# print(result)


# ========== Spot ==========
# result = client.place_spot_order(
#     product_symbol="BTC-USDT-SPOT",
#     side="buy",
#     amount="0.00004",
#     order_type="limit",
#     account="spot",
#     price="91000",
# )
# print(result)

# result = client.place_market_buy_order(
#     product_symbol="BTC-USDT-SPOT",
#     amount="6",
# )
# print(result)

# result = client.place_market_sell_order(
#     product_symbol="BTC-USDT-SPOT",
#     amount="0.00005994",
# )
# print(result)

# result = client.place_limit_buy_order(
#     product_symbol="BTC-USDT-SPOT",
#     amount="0.00006",
#     price="91000",
# )
# print(result)

# result = client.place_limit_sell_order(
#     product_symbol="BTC-USDT-SPOT",
#     amount="0.00003",
#     price="100000",
# )
# print(result)

# result = client.place_post_only_limit_buy_order(
#     product_symbol="BTC-USDT-SPOT",
#     amount="0.00006",
#     price="91000",
# )
# print(result)

# result = client.place_post_only_limit_sell_order(
#     product_symbol="BTC-USDT-SPOT",
#     amount="0.00005",
#     price="100000",
# )
# print(result)

# result = client.get_spot_order_list(
#     product_symbol="BTC-USDT-SPOT",
#     status="open",
# )
# print(result)

# result = client.cancel_spot_order()
# print(result)

# result = client.get_spot_single_order(
#     order_id="828332171796",
#     product_symbol="BTC-USDT-SPOT",
# )
# print(result)

# result = client.cancel_spot_single_order(
#     order_id="828332577400",
#     product_symbol="BTC-USDT-SPOT",
# )
# print(result)

# result = client.amend_spot_single_order(
#     order_id="828332840580",
#     product_symbol="BTC-USDT-SPOT",
#     account="spot",
#     price="91500",
# )
# print(result)

# result = client.get_spot_open_orders()
# print(result)

# result = client.place_spot_order(
#     product_symbol="BTC-USDT-SPOT",
#     side="buy",
#     amount="0.00005",
#     order_type="limit",
#     account="margin",
#     price="91000",
#     auto_borrow=True,
# )
# print(result)
