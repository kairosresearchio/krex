import krex

BITMART_API_KEY = ""
BITMART_API_SECRET = ""
MEMO = ""

client = krex.bitmart(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


# get account balance
res = client.get_account_balance()
print("1. get_account_balance:", res)


# get account currencies
res = client.get_account_currencies()
print("2. get_account_currencies:", res)


# get spot wallet
res = client.get_spot_wallet()
print("3. get_spot_wallet:", res)


# get deposit address
res = client.get_deposit_address(currency="BTC")
print("4. get_deposit_address:", res)


# get withdraw charge
res = client.get_withdraw_charge(currency="BTC")
print("5. get_withdraw_charge:", res)


# get deposit withdraw history
res = client.get_deposit_withdraw_history(currency="USDT")
print("6. get_deposit_withdraw_history:", res)


# get_deposit_withdraw_history_detail
res = client.get_deposit_withdraw_history_detail(id="26695771")
print("7. get_deposit_withdraw_history_detail:", res)


# get_contract_assets
res = client.get_contract_assets()
print("8. get_contract_assets:", res)
