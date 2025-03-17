import time
from krex.bitmart.client import Client

BITMART_API_KEY = "api_key"
BITMART_API_SECRET = "api_secret"
MEMO = "memo"

client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)


def test_get_spot_currencies():
    """Test GET https://api-cloud.bitmart.com/spot/v1/currencie"""
    assert client.get_spot_currencies()[0]["code"] == 1000


def test_get_trading_pairs():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbol"""
    assert client.get_trading_pairs()[0]["code"] == 1000


def test_GET_TRADING_PAIRS_DETAILS():
    """Test GET https://api-cloud.bitmart.com/spot/v1/symbols/details"""
    assert client.GET_TRADING_PAIRS_DETAILS()[0]["code"] == 1000


def test_get_spot_kline():
    """Test GET https://api-cloud.bitmart.com/spot/quotation/v3/lite-klines"""
    before = int(time.time())
    after = before - 3600
    assert (
        client.get_spot_kline(
            symbol="BTC_USDT", before=before, after=after, step=60, limit=5
        )[0]["code"]
        == 1000
    )


def test_get_account_currencies():
    """Test GET https://api-cloud.bitmart.com/spot/v1/walle"""
    assert client.get_account_currencies()[0]["code"] == 1000


def test_place_spot_order():
    """Test POST https://api-cloud.bitmart.com/spot/v2/submit_order"""
    assert (
        client.place_spot_order(
            symbol="BTC_USDT", side="buy", type="limit", size="0.01", price="8800"
        )[0]["code"]
        == 1000
    )


def test_place_margin_order():
    """Test POST https://api-cloud.bitmart.com/spot/v1/margin/submit_order"""
    assert (
        client.place_margin_order(
            symbol="BTC_USDT", side="buy", type="limit", size="0.01", price="8800"
        )[0]["code"]
        == 1000
    )


def test_cacel_spot_order():
    """Test POST https://api-cloud.bitmart.com/spot/v3/cancel_order"""
    assert (
        client.cacel_spot_order(symbol="BTC_USDT", client_order_id="ID125783")[0][
            "code"
        ]
        == 1000
    )


def test_get_spot_order_by_order_id():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/order"""
    assert (
        client.get_spot_order_by_order_id(
            order_id="118100034543076010", query_state="open"
        )[0]["code"]
        == 1000
    )


def test_get_spot_order_by_order_client_id():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/client-order"""
    assert (
        client.get_spot_order_by_order_client_id(
            client_order_id="118100034543076010", query_state="open"
        )[0]["code"]
        == 1000
    )


def test_get_spot_open_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/open-orders"""
    assert client.get_spot_open_orders()[0]["code"] == 1000
    assert client.get_spot_open_orders(symbol="BTC_USDT")[0]["code"] == 1000


def test_get_spot_account_orders():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/history-orders"""
    assert client.get_spot_account_orders()[0]["code"] == 1000
    assert client.get_spot_account_orders(symbol="BTC_USDT")[0]["code"] == 1000


def test_get_spot_account_trade_list():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/trades"""
    assert client.get_spot_account_trade_list()[0]["code"] == 1000
    assert client.get_spot_account_trade_list(symbol="BTC_USDT")[0]["code"] == 1000


def test_get_spot_order_trade_list():
    """Test POST https://api-cloud.bitmart.com/spot/v4/query/order-trades"""
    assert (
        client.get_spot_order_trade_list(order_id="118100034543076010")[0]["code"]
        == 1000
    )
