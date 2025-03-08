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

result = client.get_instruments(instType="SWAP")
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

result = client.set_leverage(instId="BTC-USDT-SWAP", lever="5", mgnMode="cross")
print(result)

result = client.set_leverage(instId="BTC-USDT-SWAP", lever="5", mgnMode="isolated")
print(result)

result = client.set_leverage(
    instId="BTC-USDT-SWAP", lever="5", posSide="long", mgnMode="isolated"
)
print(result)

result = client.set_position_mode(posMode="long_short_mode")
print(result)

result = client.place_order(
    instId="BTC-USDT-SWAP",
    tdMode="isolated",
    side="buy",
    posSide="net",
    ordType="limit",
    px="19000",
    sz="100",
)
print(result)
if result["code"] == "0":
    print("Successful order request，order_id = ", result["data"][0]["ordId"])
else:
    print(
        "Unsuccessful order request，error_code = ",
        result["data"][0]["sCode"],
        ", Error_message = ",
        result["data"][0]["sMsg"],
    )

result = client.place_order(
    instId="BTC-USDT-SWAP",
    tdMode="isolated",
    side="buy",
    posSide="net",
    ordType="market",
    sz="100",
)
print(result)
if result["code"] == "0":
    print("Successful order request，order_id = ", result["data"][0]["ordId"])
else:
    print(
        "Unsuccessful order request，error_code = ",
        result["data"][0]["sCode"],
        ", Error_message = ",
        result["data"][0]["sMsg"],
    )


result = client.cancel_order(instId="BTC-USDT-SWAP", ordId="505073046126960640")
print(result)

result = client.amend_order(
    instId="BTC-USDT-SWAP", ordId="505073046126960640", newSz="80"
)
print(result)

result = client.get_order(instId="BTC-USDT-SWAP", ordId="505073046126960640")
print(result)

result = client.get_order_list()
print(result)

result = client.get_orders_history(instType="SPOT")
print(result)

result = client.get_orders_history_archive(instType="SPOT")
print(result)

result = client.get_fills(instType="SWAP")
print(result)

result = client.get_fills_history(instType="SWAP")
print(result)

result = client.get_positions()
print(result)
