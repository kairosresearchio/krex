import os
from dotenv import load_dotenv
from krex.gateio.client import Client

load_dotenv()


client = Client(
    api_key=os.getenv("GATEIO_APIKEY"),
    api_secret=os.getenv("GATEIO_APISECRET"),
)

result = client.get_futures_account()
print(result)

result = client.get_futures_account_book()
print(result)

result = client.get_delivery_account()
print(result)

result = client.get_delivery_account_book()
print(result)

result = client.get_spot_account(ccy="btc")
print(result)

result = client.get_spot_account_book()
print(result)
