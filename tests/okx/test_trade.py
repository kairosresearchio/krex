import unittest
from krex.okx.client import Client

OKX_API_KEY = "api_key"
OKX_API_SECRET = "api_secret"
OKX_PASSPHRASE = "passphrase"

# flag = "1" for test environment
# flag = "0" for production environment
FLAG = "1"
client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
    flag=FLAG,
)


class TradeTest(unittest.TestCase):
    def test_place_order(self):
        attachAlgoOrds = [
            {
                "tpTriggerPx": "49000.0",
                "tpOrdPx": "-1",
                "sz": "1",
                "tpTriggerPxType": "last",
            }
        ]
        result = client.place_order(
            "BTC-USDT-SWAP",
            tdMode="isolated",
            clOrdId="asCai1234",
            side="buy",
            posSide="long",
            ordType="limit",
            sz="1",
            px="30000.0",
            attachAlgoOrds=attachAlgoOrds,
        )
        print(result)
        self.assertEqual(result.get("code"), "0")

    def test_get_order_info(self):
        result = client.get_order("ETH-USDT", "480707205436669952")
        print(result)
        self.assertEqual(result.get("code"), "0")


if __name__ == "__main__":
    unittest.main()
