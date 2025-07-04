from krex.bybit.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

client = Client(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)


def test_get_open_orders():
    res = client.get_open_orders(category="spot")
    assert res is not None


def test_get_order_history():
    res = client.get_order_history()
    assert res is not None


def test_get_execution_list():
    res = client.get_execution_list()
    assert res is not None


def test_get_borrow_quota():
    res = client.get_borrow_quota(product_symbol="BTC-USDT-SWAP", side="Buy")
    assert res is not None


def test_get_vip_margin_data():
    res = client.get_vip_margin_data()
    assert res is not None


def test_get_collateral():
    res = client.get_collateral()
    assert res is not None


def test_get_historical_interest_rate():
    res = client.get_historical_interest_rate(currency="USDT")
    assert res is not None


def test_get_status_and_leverage():
    res = client.get_status_and_leverage()
    assert res is not None
