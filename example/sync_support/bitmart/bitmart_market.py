from krex.bitmart.client import Client
from datetime import datetime, timedelta

client = Client()


# get account balance
res = client.get_spot_currencies()
print("1. get_spot_currencies:", res)


# get account currencies
res = client.get_trading_pairs()
print("2. get_trading_pairs:", res)


# get spot wallet
res = client.get_trading_pairs_details()
print("3. get_trading_pairs_details:", res)


# get deposit address
res = client.get_ticker_of_all_pairs()
print("4. get_ticker_of_all_pairs:", res)


# get_ticker_of_a_pair
res = client.get_ticker_of_a_pair(product_symbol="BTC-USDT-SPOT")
print("5. get_ticker_of_a_pair:", res)


# get_spot_kline
res = client.get_spot_kline("BTC-USDT-SPOT", "5m")
print("6. get_spot_kline:", res)

# get_contracts_details
res = client.get_contracts_details()
print("7. get_contracts_details:", res)

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
