from krex.okx.client import Client

OKX_API_KEY = "api_key"
OKX_API_SECRET = "api_secret"
OKX_PASSPHRASE = "passphrase"

# flag = "1" for test environment
# flag = "0" for production environment
FLAG = "0"
client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
    flag=FLAG,
)


result = client.get_currencies()
print(result)


result = client.get_account_balance()
print(result)

result = client.get_instruments(instType="SPOT")
print(result)

result = client.get_max_avail_size(instId="BTC-USDT", tdMode="cash")
print(result)

result = client.get_account_config()
print(result)
if result["code"] == "0":
    acctLv = result["data"][0]["acctLv"]
    modes = {
        "1": "Simple mode",
        "2": "Single-currency margin mode",
        "3": "Multi-currency margin mode",
        "4": "Portfolio margin mode",
    }
    print(modes.get(acctLv, "unknown mode"))

result = client.place_order(instId="BTC-USDT", tdMode="cash", side="buy", ordType="limit", px="19000", sz="0.01")
print(result)

result = client.place_order(instId="BTC-USDT", tdMode="cash", side="buy", ordType="market", sz="100")
print(result)

result = client.cancel_order(instId="BTC-USDT", ordId="489093931993509888")
print(result)

result = client.get_order_list()
print(result)

result = client.get_orders_history(instType="SPOT")
print(result)

result = client.place_algo_order(
    instId="BTC-USDT",
    tdMode="cash",
    side="buy",
    ordType="trigger",
    sz="100",
    triggerPx="10000",
    orderPx="-1",
    triggerPxType="last",
)
print(result)

algo_orders = [{"instId": "BTC-USDT", "algoId": "495001187587043328"}]
result = client.cancel_algo_order(algo_orders)
print(result)

result = client.order_algos_history(ordType="conditional", state="canceled")
print(result)
