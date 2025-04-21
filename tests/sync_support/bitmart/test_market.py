from datetime import datetime, timedelta
from krex.bitmart.client import Client

BITMART_API_KEY = "613c8332848ff6b83aa915ae6270f2e842901036"
BITMART_API_SECRET = "66b82353bfee263185b36bdcaa244ee805c68aa87fd593addcd5124ff334ea3f"
MEMO = "trade"


client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


def test_get_spot_currencies():
    res = client.get_spot_currencies()
    assert res is not None


def test_get_trading_pairs():
    res = client.get_trading_pairs()
    assert res is not None


def test_get_trading_pairs_details():
    res = client.get_trading_pairs_details()
    assert res is not None


def test_get_ticker_of_all_pairs():
    res = client.get_ticker_of_all_pairs()
    assert res is not None


def test_get_ticker_of_a_pair():
    res = client.get_ticker_of_a_pair(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_spot_kline():
    res = client.get_spot_kline("BTC-USDT-SPOT", "5m")
    assert res is not None


def test_get_depth():
    res = client.get_depth(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_contract_kline():
    start = int((datetime.now() - timedelta(days=1)).timestamp())
    end = int(datetime.now().timestamp())
    res = client.get_contract_kline("BTC-USDT-SWAP", "5m", start, end)
    assert res is not None
