from krex.binance.client import Client

BINANCE_APIKEY = "ovqxr2nXR50oeKo47CVKZTZ7ZmaCY3y1q7iAEOfsDXliAv52koJIcHEtlHDH30AU"
BINANCE_APISECRET = "sZ4nwX3owfZNDu4qBu0Y4H8zbic4E6FLtkbbNytV5Z6S77ZTiCgGxgYxHVitq4GQ"

client = Client(
    api_key=BINANCE_APIKEY,
    api_secret=BINANCE_APISECRET,
)

result = client.get_account_balance()
print(result)

result = client.get_income_history()
print(result)
