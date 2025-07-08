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


def test_get_wallet_summary(client):
    res = client.get_wallet_summary()
    assert res is not None
