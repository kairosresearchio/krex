import krex
import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")


client = krex.bybit(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

result = client.get_wallet_balance()
print(result)

result = client.get_transferable_amount(coins=["BTC", "ETH"])
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
