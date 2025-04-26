from krex.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"

client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
)

result = client.get_currencies()
print(result)

result = client.get_balances()
print(result)

result = client.get_asset_valuation()
print(result)

result = client.get_bills()
print(result)

result = client.get_deposit_address(ccy="BTC")
print(result)

result = client.get_deposit_history()
print(result)

result = client.get_bills()
print(result)

result = client.get_withdrawal_history()
print(result)

result = client.get_exchange_list()
print(result)

result = client.post_monthly_statement(month="Mar")
print(result)

result = client.get_monthly_statement(month="Mar")
print(result)

result = client.get_convert_currencies()
print(result)
