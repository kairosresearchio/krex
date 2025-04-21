from krex.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"

client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
)


def test_get_order_list():
    res = client.get_order_list(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_orders_history():
    res = client.get_orders_history(instType="SPOT")
    assert res is not None


def test_get_orders_history_archive():
    res = client.get_orders_history_archive(instType="SPOT")
    assert res is not None


def test_get_fills():
    res = client.get_fills()
    assert res is not None


def test_get_fills_history():
    res = client.get_fills_history(instType="SPOT")
    assert res is not None


def test_get_account_rate_limit():
    res = client.get_account_rate_limit()
    assert res is not None
