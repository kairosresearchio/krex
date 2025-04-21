from krex.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"

client = Client(
    api_key=OKX_API_KEY,
    api_secret=OKX_API_SECRET,
    passphrase=OKX_PASSPHRASE,
)


def test_get_public_instruments():
    res = client.get_public_instruments(instType="SPOT")
    assert res is not None


def test_get_funding_rate():
    res = client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_funding_rate_history():
    res = client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None
