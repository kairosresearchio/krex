import time

from krex.http.bitmart.client import Client

BITMART_API_KEY = "api_key"
BITMART_API_SECRET = "api_secret"
MEMO = "memo"

client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


def test_get_account_currencies():
    """Test GET https://api-cloud.bitmart.com/account/v1/currencie"""
    assert client.get_account_currencies()[0]["code"] == 1000
    assert client.get_account_currencies(currencies="BTC,ETH")[0]["code"] == 1000


def test_get_account_balance():
    """Test GET https://api-cloud.bitmart.com/account/v1/wallet"""
    assert client.get_account_balance(currency="BTC")[0]["code"] == 1000


def test_get_deposit_address():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit/address"""
    assert client.get_deposit_address(currency="USDT-ERC20")[0]["code"] == 1000


def test_get_withdraw_charge():
    """Test GET https://api-cloud.bitmart.com/account/v1/withdraw/charge"""
    assert client.get_withdraw_charge(currency="USDT-ERC20")[0]["code"] == 1000


def test_post_withdraw_apply():
    """Test POST https://api-cloud.bitmart.com/account/v1/withdraw/apply"""
    assert (
        client.post_withdraw_apply(
            currency="USDT-ERC20",
            amount="40",
            destination="To Digital Address",
            address="0xe57b69a8776b37860407965B73cdFFBDFe668Bb5",
            address_memo="",
        )[0]["code"]
        == 1000
    )


def test_get_deposit_withdraw_history():
    """Test GET https://api-cloud.bitmart.com/account/v2/deposit-withdraw/history"""
    after = int(time.time())
    before = after - 3600
    assert (
        client.get_deposit_withdraw_history(
            currency="USDT-ERC20",
            operation_type="withdraw",
            n=10,
            start_time=before,
            end_time=after,
        )[0]["code"]
        == 1000
    )


def test_get_deposit_withdraw_history_detail():
    """Test GET https://api-cloud.bitmart.com/account/v1/deposit-withdraw/detail"""
    assert client.get_deposit_withdraw_history_detail(id="1680001")[0]["code"] == 1000
