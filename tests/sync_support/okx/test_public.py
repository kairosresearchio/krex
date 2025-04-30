from krex.okx.client import Client


client = Client()


def test_get_public_instruments():
    res = client.get_public_instruments(instType="SPOT")
    assert res is not None


def test_get_funding_rate():
    res = client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_funding_rate_history():
    res = client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None
