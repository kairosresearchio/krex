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


class AssetTest(unittest.TestCase):
    def test_get_currencies(self):
        result = client.get_currencies(ccy="BTC")
        self.assertEqual(result.get("code"), "0")

    def test_get_balances(self):
        result = client.get_balances()
        self.assertEqual(result.get("code"), "0")

    def test_get_non_tradable_assets(self):
        result = client.get_non_tradable_assets()
        self.assertEqual(result.get("code"), "0")

    def test_get_asset_valuation(self):
        result = client.get_asset_valuation(ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_funds_transfer(self):
        result = client.funds_transfer(ccy="USDT", amt="100", from_="6", to="18")
        self.assertEqual(result.get("code"), "0")

    def test_transfer_state(self):
        result = client.transfer_state(transId="11")
        self.assertEqual(result.get("code"), "0")

    def test_get_bills(self):
        result = client.get_bills()
        self.assertEqual(result.get("code"), "0")

    def test_get_deposit_address(self):
        result = client.get_deposit_address(ccy="BTC")
        self.assertEqual(result.get("code"), "0")

    def test_get_deposit_history(self):
        result = client.get_deposit_history()
        self.assertEqual(result.get("code"), "0")

    def test_withdrawal(self):
        result = client.withdrawal(
            ccy="USDT",
            amt="1",
            dest="3",
            toAddr="18740405107",
            areaCode="86",
        )
        self.assertEqual(result.get("code"), "0")

    def test_cancel_withdrawal(self):
        result = client.cancel_withdrawal(wdId="sdhiadhsfdjknvjdaodns")
        self.assertEqual(result.get("code"), "0")

    def test_get_withdrawal_history(self):
        result = client.get_withdrawal_history()
        self.assertEqual(result.get("code"), "0")

    def test_get_deposit_withdraw_status(self):
        result = client.get_deposit_withdraw_status(wdId="84804812")
        self.assertEqual(result.get("code"), "0")

    def test_get_deposit_lightning(self):
        result = client.get_deposit_lightning(ccy="BTC", amt="10")
        self.assertEqual(result.get("code"), "0")

    def test_withdrawal_lightning(self):
        rcvrInfo = {
            "walletType": "exchange",
            "exchId": "did:ethr:0xfeb4f99829a9acdf52979abee87e83addf22a7e1",
            "rcvrFirstName": "Bruce",
            "rcvrLastName": "Wayne",
            "rcvrCountry": "United States",
            "rcvrCountrySubDivision": "California",
            "rcvrTownName": "San Jose",
            "rcvrStreetName": "Clementi Avenue 1",
        }
        result = client.withdrawal_lightning(
            ccy="BTC",
            invoice="lnbc100u1psnnvhtpp5yq2x3q5hhrzsuxpwx7ptphwzc4k4wk0j3stp0099968m44cyjg9sdqqcqzpgxqzjcsp5hz",
            rcvrInfo=rcvrInfo,
        )
        self.assertEqual(result.get("code"), "0")


if __name__ == "__main__":
    unittest.main()
