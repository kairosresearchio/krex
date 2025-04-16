import unittest
from krex.http.bybit.client import Client

BYBIT_API_KEY = "api_key"
BYBIT_API_SECRET = "api_secret"
TESTNET = False  # True means your API keys were generated on testnet.bybit.com

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
    testnet=TESTNET,
)


class HTTPTest(unittest.TestCase):
    def test_get_wallet_balance(self):
        result = client.get_wallet_balance()
        print(result)
        self.assertEqual(result.get("retCode"), 0)


if __name__ == "__main__":
    unittest.main()
