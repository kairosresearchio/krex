from krex.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"

client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
)


def test_get_currencies():
    res = client.get_currencies()
    assert res is not None


def test_get_balances():
    res = client.get_balances()
    assert res is not None


def test_get_asset_valuation():
    res = client.get_asset_valuation()
    assert res is not None


def test_get_bills():
    res = client.get_bills()
    assert res is not None


def test_get_deposit_address():
    res = client.get_deposit_address(ccy="BTC")
    assert res is not None


def test_get_deposit_history():
    res = client.get_deposit_history()
    assert res is not None


def test_get_withdrawal_history():
    res = client.get_withdrawal_history()
    assert res is not None


def test_get_exchange_list():
    res = client.get_exchange_list()
    assert res is not None


def test_post_monthly_statement():
    res = client.post_monthly_statement(month="Mar")
    assert res is not None


def test_get_monthly_statement():
    res = client.get_monthly_statement(month="Mar")
    assert res is not None


def test_get_convert_currencies():
    res = client.get_convert_currencies()
    assert res is not None
