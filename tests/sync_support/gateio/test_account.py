import os
from dotenv import load_dotenv
from krex.gateio.client import Client

load_dotenv()

client = Client(
    api_key=os.getenv("GATEIO_API_KEY"),
    api_secret=os.getenv("GATEIO_API_SECRET"),
)


def test_get_futures_account():
    res = client.get_futures_account()
    assert res is not None


def test_get_futures_account_book():
    res = client.get_futures_account_book()
    assert res is not None


def test_get_delivery_account():
    res = client.get_delivery_account()
    assert res is not None


def test_get_delivery_account_book():
    res = client.get_delivery_account_book()
    assert res is not None


def test_get_spot_account():
    res = client.get_spot_account(ccy="btc")
    assert res is not None


def test_get_spot_account_book():
    res = client.get_spot_account_book()
    assert res is not None
