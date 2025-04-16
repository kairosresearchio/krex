from krex.http.bybit.client import Client


BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = False  # True means your API keys were generated on testnet.bybit.com

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)

response = client.place_order(
    category="spot",
    symbol="ETHUSDT",
    side="Sell",
    orderType="Market",
    qty="0.1",
    timeInForce="GTC",
)

response = client.get_open_orders(
    category="linear",
    symbol="BTCUSDT",
)

orders = response["result"]["list"]

for order in orders:
    if order["orderStatus"] == "Untriggered":
        client.cancel_order(
            category="linear",
            symbol=order["symbol"],
            orderId=order["orderId"],
        )


orders_to_cancel = [
    {"category": "option", "symbol": o["symbol"], "orderId": o["orderId"]}
    for o in response["result"]["list"]
    if o["orderStatus"] == "New"
]

response = client.cancel_batch_order(
    category="option",
    request=orders_to_cancel,
)
