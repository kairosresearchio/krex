from krex.bybit.client import Client

client = Client()


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
