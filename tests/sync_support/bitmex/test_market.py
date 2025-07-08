import pytest
from krex.bitmex.client import Client


@pytest.fixture
def client():
    return Client()


def test_get_instrument_info(client):
    res = client.get_instrument_info()
    assert res is not None


def test_get_instrument_info_with_symbol(client):
    res = client.get_instrument_info(product_symbol="XBT-USDT-SWAP")
    assert res is not None


def test_get_orderbook(client):
    res = client.get_orderbook(product_symbol="XBT-USDT-SWAP")
    assert res is not None


def test_get_trades(client):
    res = client.get_trades(product_symbol="XBT-USDT-SWAP", count=10)
    assert res is not None


def test_get_ticker(client):
    res = client.get_ticker(symbol="XBT-USDT-SWAP", binSize="1m", count=5)
    assert res is not None


def test_get_kline(client):
    res = client.get_kline(symbol="XBT-USDT-SWAP", binSize="1m", count=5)
    assert res is not None


def test_get_funding(client):
    res = client.get_funding(product_symbol="XBT-USDT-SWAP", count=10)
    assert res is not None
