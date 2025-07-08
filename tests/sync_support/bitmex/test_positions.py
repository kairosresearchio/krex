import pytest
from krex.bitmex.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")


@pytest.fixture
def client():
    return Client(
        api_key=BITMEX_API_KEY,
        api_secret=BITMEX_API_SECRET,
    )


def test_get_positions(client):
    res = client.get_positions()
    assert res is not None


def test_switch_mode(client):
    res = client.switch_mode(product_symbol="XBT-USDT-SWAP", enabled=True)
    assert res is not None


def test_set_leverage(client):
    res = client.set_leverage(product_symbol="XBT-USDT-SWAP", leverage=10.0, cross_margin=False)
    assert res is not None


def test_set_margining_mode(client):
    res = client.set_margining_mode(multi_asset=False)
    assert res is not None


def test_get_margining_mode(client):
    res = client.get_margining_mode()
    assert res is not None


def test_get_margin(client):
    res = client.get_margin()
    assert res is not None
