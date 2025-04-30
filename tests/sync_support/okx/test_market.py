from krex.okx.client import Client

client = Client()


def test_get_candles_ticks():
    res = client.get_candles_ticks(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_orderbook():
    res = client.get_orderbook(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_tickers():
    res = client.get_tickers(instType="SPOT")
    assert res is not None
