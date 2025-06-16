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

result = client.get_coin_info()
print(result)

# result = client.get_sub_uid()
# print(result)

result = client.get_spot_asset_info()
print(result)

result = client.get_coins_balance(accountType="FUND")
print(result)

result = client.get_coin_balance(accountType="FUND", coin="BTC")
print(result)

result = client.get_withdrawable_amount(coin="USDT")
print(result)

result = client.get_internal_transfer_records()
print(result)

result = client.get_universal_transfer_records()
print(result)

result = client.get_deposit_records()
print(result)

result = client.get_internal_deposit_records()
print(result)

# result = client.get_master_deposit_address(coin="USDT")
# print(result)

result = client.get_withdrawal_records()
print(result)

# result = client.get_transferable_coin(
#     fromAccountType="FUND",
#     toAccountType="UNIFIED",
# )
# print(result)

# result = client.create_internal_transfer(
#     coin="USDT",
#     amount="1",
#     fromAccountType="UNIFIED",
#     toAccountType="FUND",
# )
# print(result)
