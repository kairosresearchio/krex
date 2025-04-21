from krex.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)


def test_get_instruments_info():
    res = client.get_instruments_info(category="spot")
    assert res is not None


def test_get_kline():
    res = client.get_kline(
        product_symbol="BTC-USDT-SPOT",
        interval="1m",
    )
    assert res is not None


def test_get_orderbook():
    res = client.get_orderbook(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_tickers():
    res = client.get_tickers()
    assert res is not None


def test_get_funding_rate_history():
    res = client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None
