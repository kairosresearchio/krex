from krex.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

result = client.get_wallet_balance()
print(result)

result = client.get_transferable_amount()
print(result)

# result = client.upgrade_to_unified_trading_account()
# print(result)

result = client.get_borrow_history()
print(result)

result = client.get_collateral_info()
print(result)

result = client.get_fee_rates()
print(result)

result = client.get_account_info()
print(result)

result = client.get_transaction_log()
print(result)

# result = client.set_collateral_coin("BTC", "ON")
# print(result)

# result = client.set_margin_mode("PORTFOLIO_MARGIN")
# print(result)

# # need test
# result = client.repay_liability()
# print(result)
