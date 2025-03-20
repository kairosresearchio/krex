import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT)
from krex.bitmart.client import Client

BITMART_API_KEY = "613c8332848ff6b83aa915ae6270f2e842901036"
BITMART_API_SECRET = "66b82353bfee263185b36bdcaa244ee805c68aa87fd593addcd5124ff334ea3f"
MEMO = "trade"

client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


# get account balance
res = client.get_account_balance()
print("1. get_account_balance:", res)

print("\n#######################\n")

# get account currencies
res = client.get_account_currencies()
print("2. get_account_currencies:", res)

print("\n#######################\n")

# get spot wallet
res = client.get_spot_wallet()
print("3. get_spot_wallet:", res)

print("\n#######################\n")

# get deposit address
res = client.get_deposit_address(currency="USDT-TRC20")
print("4. get_deposit_address:", res)

print("\n#######################\n")

# get withdraw charge
# res = client.get_withdraw_charge(currency="USDT-TRC20")
# print("5. get_withdraw_charge:", res)

print("\n#######################\n")

# get deposit withdraw history
res = client.get_deposit_withdraw_history(currency="USDT")
print("6. get_deposit_withdraw_history:", res)

print("\n#######################\n")

# get_deposit_withdraw_history_detail
res = client.get_deposit_withdraw_history_detail(id="26695771")
print("7. get_deposit_withdraw_history_detail:", res)

print("\n#######################\n")

# get_contract_assets
res = client.get_contract_assets()
print("8. get_contract_assets:", res)




