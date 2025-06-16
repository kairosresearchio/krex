from krex.binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()


BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(
    api_key=BINANCE_API_KEY,
    api_secret=BINANCE_API_SECRET,
)


def test_get_account_balance():
    res = client.get_account_balance()
    assert res is not None


def test_get_income_history():
    res = client.get_income_history()
    assert res is not None
