from krex.bybit.client import Client

BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = True

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)

print(
    client.place_order(
        category="linear",
        symbol="BTCUSDT",
        side="Buy",
        orderType="Market",
        qty="0.001",
    )
)
