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


def test_get_positions():
    res = client.get_positions(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_closed_pnl():
    res = client.get_closed_pnl()
    assert res is not None
