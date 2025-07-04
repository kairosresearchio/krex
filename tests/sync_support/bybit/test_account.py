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


def test_get_wallet_balance():
    res = client.get_wallet_balance()
    assert res is not None


def test_get_transferable_amount():
    res = client.get_transferable_amount(coins=["BTC", "ETH"])
    assert res is not None


def test_get_borrow_history():
    res = client.get_borrow_history()
    assert res is not None


def test_get_collateral_info():
    res = client.get_collateral_info()
    assert res is not None


def test_get_fee_rates():
    res = client.get_fee_rates()
    assert res is not None


def test_get_account_info():
    res = client.get_account_info()
    assert res is not None


def test_get_transaction_log():
    res = client.get_transaction_log()
    assert res is not None
