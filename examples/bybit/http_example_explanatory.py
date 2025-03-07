from krex.bybit.client import Client

import logging

logging.basicConfig(
    filename="bybit.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)


BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = True

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)

print(client.get_wallet_balance(accountType="UNIFIED"))

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
