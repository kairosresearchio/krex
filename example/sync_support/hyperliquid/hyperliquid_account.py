from krex.hyperliquid.client import Client


client = Client()

wallet_address = "0x8C41a1cB41bbEC8108E5E421007E17b8336E17dE"

result = client.clearinghouse_state(
    user= wallet_address
)
print(result)

result = client.open_orders(
    user= wallet_address
)
print(result)

result = client.user_fills(
    user= wallet_address
)
print(result)

result = client.user_rate_limit(
    user= wallet_address
)
print(result)

result = client.order_status(
    user= wallet_address,
    oid= ""
)
print(result)

result = client.historical_orders(
    user= wallet_address
)
print(result)

result = client.subaccounts(
    user= wallet_address
)
print(result)

result = client.user_role(
    user= wallet_address
)
print(result)

result = client.portfolio(
    user= wallet_address
)
print(result)