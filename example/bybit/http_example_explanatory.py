from krex.bybit.client import Client

BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = False  # True means your API keys were generated on testnet.bybit.com

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)

print(client.get_wallet_balance())

print(
    client.place_order(
        category="linear",
        symbol="BTCUSDT",
        side="Buy",
        orderType="Market",
        qty="0.001",
    )
)

print(
    client.place_order(
        category="inverse",
        symbol="ETHUSD",
        side="Buy",
        orderType="Market",
        qty="1",
    )
)

print(
    client.place_order(
        category="spot",
        symbol="MNTUSDT",
        side="Buy",
        orderType="Market",
        qty="10",
    )
)
