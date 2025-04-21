from krex.bitmart.client import Client

BITMART_API_KEY = "613c8332848ff6b83aa915ae6270f2e842901036"
BITMART_API_SECRET = "66b82353bfee263185b36bdcaa244ee805c68aa87fd593addcd5124ff334ea3f"
MEMO = "trade"


client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


def test_get_account_balance():
    res = client.get_account_balance()
    assert res is not None


def test_get_account_currencies():
    res = client.get_account_currencies()
    assert res is not None


def test_get_spot_wallet():
    res = client.get_spot_wallet()
    assert res is not None


def test_get_deposit_address():
    res = client.get_deposit_address(currency="BTC")
    assert res is not None


# def test_get_withdraw_charge():
#     res = client.get_withdraw_charge(currency="BTC")
#     assert res is not None


def test_get_deposit_withdraw_history():
    res = client.get_deposit_withdraw_history(currency="USDT")
    assert res is not None


def test_get_deposit_withdraw_history_detail():
    res = client.get_deposit_withdraw_history_detail(id="26695771")
    assert res is not None


def test_get_contract_assets():
    res = client.get_contract_assets()
    assert res is not None
