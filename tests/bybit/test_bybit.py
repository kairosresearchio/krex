import unittest
from krex.bybit.client import Client

BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = True

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)


class HTTPTest(unittest.TestCase):
    # We can't really test authenticated endpoints without keys, but we
    # can make sure it raises a PermissionError.
    def test_place_active_order(self):
        with self.assertRaises(PermissionError):
            client.place_order(
                symbol="BTCUSD",
                order_type="Market",
                side="Buy",
                qty=1,
                category="spot",
            )
