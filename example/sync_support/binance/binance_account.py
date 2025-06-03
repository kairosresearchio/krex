import krex

BINANCE_APIKEY = ""
BINANCE_APISECRET = ""

client = krex.binance(
    api_key=BINANCE_APIKEY,
    api_secret=BINANCE_APISECRET,
)

result = client.get_account_balance()
print(result)

result = client.get_income_history()
print(result)
