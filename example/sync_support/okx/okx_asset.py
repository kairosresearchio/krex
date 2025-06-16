import krex
import os
from dotenv import load_dotenv

load_dotenv()

OKX_API_KEY = os.getenv("OKX_API_KEY")
OKX_API_SECRET = os.getenv("OKX_API_SECRET")
OKX_PASSPHRASE = os.getenv("OKX_PASSPHRASE")

client = krex.okx(
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
