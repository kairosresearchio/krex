from krex.binance.client import Client


client = Client()


def test_get_spot_exchange_info():
    res = client.get_spot_exchange_info(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_futures_exchange_info():
    res = client.get_futures_exchange_info()
    assert res is not None


def test_get_futures_ticker():
    res = client.get_futures_ticker(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_futures_kline():
    res = client.get_futures_kline(product_symbol="BTC-USDT-SWAP", interval="1m")
    assert res is not None


def test_get_futures_premium_index():
    res = client.get_futures_premium_index(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_futures_funding_rate():
    res = client.get_futures_funding_rate(product_symbol="BTC-USDT-SWAP")
    assert res is not None
