from krex.http.bitmart.client import Client
from datetime import datetime, timedelta

BITMART_API_KEY = "613c8332848ff6b83aa915ae6270f2e842901036"
BITMART_API_SECRET = "66b82353bfee263185b36bdcaa244ee805c68aa87fd593addcd5124ff334ea3f"
MEMO = "trade"

client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


# get account balance
res = client.get_spot_currencies()
print("1. get_spot_currencies:", res)

print("\n#######################\n")

# get account currencies
res = client.get_trading_pairs()
print("2. get_trading_pairs:", res)

print("\n#######################\n")

# get spot wallet
res = client.get_trading_pairs_details()
print("3. get_trading_pairs_details:", res)

print("\n#######################\n")

# get deposit address
res = client.get_ticker_of_all_pairs()
print("4. get_ticker_of_all_pairs:", res)

print("\n#######################\n")

# get_ticker_of_a_pair
res = client.get_ticker_of_a_pair(product_symbol="BTC-USDT-SPOT")
print("5. get_ticker_of_a_pair:", res)

print("\n#######################\n")

# get_spot_kline
res = client.get_spot_kline("BTC-USDT-SPOT", "5m")
print("6. get_spot_kline:", res)

# get_contracts_details
# res = client.get_contracts_details()
# print("7. get_contracts_details:", res)

# get_depth
res = client.get_depth(product_symbol="BTC-USDT-SWAP")
print("8. get_depth:", res)

# get_contract_kline
res = client.get_contract_kline(
    "BTC-USDT-SWAP",
    "5m",
    int((datetime.now() - timedelta(days=1)).timestamp()),
    int(datetime.now().timestamp()),
)

print("9. get_contract_kline:", res)
