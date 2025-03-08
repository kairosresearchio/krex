import unittest
from krex.okx.client import Client

OKX_API_KEY = "api_key"
OKX_API_SECRET = "api_secret"
OKX_PASSPHRASE = "passphrase"

# 設定環境：實盤交易 = "0"，模擬交易 = "1"
FLAG = "1"
client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
    flag=FLAG,
)


class AccountTest(unittest.TestCase):
    def test_get_instruments(self):
        result = client.get_instruments(instType="SPOT")
        self.assertEqual(result.get("code"), "0")

    def test_get_account_balance(self):
        result = client.get_account_balance(ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_get_positions(self):
        result = client.get_positions(instType="SWAP")
        self.assertEqual(result.get("code"), "0")

    def test_get_positions_history(self):
        result = client.get_positions_history(instType="SWAP")
        self.assertEqual(result.get("code"), "0")

    def test_get_position_risk(self):
        result = client.get_position_risk(instType="SWAP")
        self.assertEqual(result.get("code"), "0")

    def test_get_account_bills(self):
        result = client.get_account_bills(instType="SPOT")
        self.assertEqual(result.get("code"), "0")

    def test_get_account_bills_archive(self):
        result = client.get_account_bills_archive(
            begin="1715780962300", end="1716998400000"
        )
        self.assertEqual(result.get("code"), "0")

    def test_get_account_config(self):
        result = client.get_account_config()
        self.assertEqual(result.get("code"), "0")

    def test_set_position_mode(self):
        result = client.set_position_mode(posMode="net_mode")
        self.assertEqual(result.get("code"), "0")

    def test_set_leverage(self):
        result = client.set_leverage(lever="5", mgnMode="isolated", instId="BTC-USDT")
        self.assertEqual(result.get("code"), "0")

    def test_get_max_order_size(self):
        result = client.get_max_order_size(instId="BTC-USDT", tdMode="cash")
        self.assertEqual(result.get("code"), "0")

    def test_get_max_avail_size(self):
        result = client.get_max_avail_size(instId="BTC-USDT", tdMode="cash")
        self.assertEqual(result.get("code"), "0")

    def test_adjustment_margin(self):
        result = client.adjustment_margin(
            instId="BTC-USDT-SWAP", posSide="net", type="add", amt="1"
        )
        self.assertEqual(
            result.get("code"), "59300"
        )  # 59300: The position is not found

    def test_get_leverage(self):
        result = client.get_leverage(mgnMode="cross", ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_get_max_loan(self):
        result = client.get_max_loan(
            mgnMode="cross", instId="BTC-USDT", ccy="BTC", mgnCcy="USDT"
        )
        self.assertEqual(result.get("code"), "0")

    def test_get_fee_rates(self):
        result = client.get_fee_rates(instType="SPOT")
        self.assertEqual(result.get("code"), "0")

    def test_get_interest_accrued(self):
        result = client.get_interest_accrued()
        self.assertEqual(result.get("code"), "0")

    def test_get_interest_rate(self):
        result = client.get_interest_rate(ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_set_greeks(self):
        result = client.set_greeks(greeksType="BS")
        self.assertEqual(result.get("code"), "0")

    def test_set_isolated_mode(self):
        result = client.set_isolated_mode(isoMode="automatic", type="MARGIN")
        self.assertEqual(result.get("code"), "51010")

    def test_get_max_withdrawal(self):
        result = client.get_max_withdrawal(ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_get_account_position_risk(self):
        result = client.get_account_position_risk()
        self.assertEqual(result.get("code"), "0")

    def test_get_interest_limits(self):
        result = client.get_interest_limits(ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_spot_manual_borrow_repay(self):
        result = client.spot_manual_borrow_repay(ccy="USDT", side="borrow", amt=1)
        self.assertEqual(result.get("code"), "59410")

    def test_set_auto_repay(self):
        result = client.set_auto_repay(autoRepay=True)
        self.assertEqual(result.get("code"), "51010")

    def test_spot_borrow_repay_history(self):
        result = client.spot_borrow_repay_history(
            ccy="USDT", type="auto_borrow", after="1597026383085"
        )
        self.assertEqual(result.get("code"), "0")

    def test_position_builder(self):
        sim_pos = [
            {"instId": "BTC-USDT-SWAP", "pos": "10", "avgPx": "100000"},
            {"instId": "ETH-USDT-SWAP", "pos": "10", "avgPx": "3000"},
        ]
        sim_asset = [{"ccy": "USDT", "amt": "1000000"}]

        result = client.position_builder(
            inclRealPosAndEq=False,
            simPos=sim_pos,
            simAsset=sim_asset,
            greeksType="CASH",
        )
        self.assertEqual(result.get("code"), "0")

    def test_get_greeks(self):
        result = client.get_greeks(ccy="USDT")
        self.assertEqual(result.get("code"), "0")

    def test_get_account_position_tiers(self):
        result = client.get_account_position_tiers(
            instType="SWAP", instFamily="BTC-USDT"
        )
        self.assertEqual(result.get("code"), "0")

    def test_activate_option(self):
        result = client.activate_option()
        self.assertEqual(result.get("code"), "50050")

    def test_set_auto_loan(self):
        result = client.set_auto_loan(autoLoan="true")
        self.assertEqual(result.get("code"), "0")

    def test_set_account_level(self):
        result = client.set_account_level(acctLv="2")
        self.assertEqual(result.get("code"), "59001")

    def test_get_simulated_margin(self):
        result = client.get_simulated_margin(instType="SWAP")
        self.assertEqual(result.get("code"), 404)

    def test_borrow_repay(self):
        result = client.borrow_repay(ccy="BTC", side="borrow", amt="1.0")
        self.assertEqual(result.get("code"), "0")

    def test_borrow_repay_history(self):
        result = client.borrow_repay_history(ccy="BTC")
        self.assertEqual(result.get("code"), "0")

    def test_get_vip_interest_accrued_data(self):
        result = client.get_vip_interest_accrued_data(ccy="BTC")
        self.assertEqual(result.get("code"), "0")

    def test_get_vip_interest_deducted_data(self):
        result = client.get_vip_interest_deducted_data(ccy="BTC")
        self.assertEqual(result.get("code"), "0")

    def test_get_vip_loan_order_list(self):
        result = client.get_vip_loan_order_list(ccy="BTC")
        self.assertEqual(result.get("code"), "0")

    def test_get_vip_loan_order_detail(self):
        result = client.get_vip_loan_order_detail(ccy="BTC", ordId="1")
        self.assertEqual(result.get("code"), "0")


if __name__ == "__main__":
    unittest.main()
