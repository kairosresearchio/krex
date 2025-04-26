import os
from dotenv import load_dotenv
from krex.gateio.client import Client

load_dotenv()

client = Client(
    api_key=os.getenv("GATEIO_APIKEY"),
    api_secret=os.getenv("GATEIO_APISECRET"),
)


def test_get_all_futures_contracts():
    res = client.get_all_futures_contracts()
    assert res is not None


def test_get_a_single_futures_contract():
    res = client.get_a_single_futures_contract(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_contract_order_book_futures():
    res = client.get_contract_order_book(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_contract_kline_futures():
    res = client.get_contract_kline(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_contract_list_tickers_futures():
    res = client.get_contract_list_tickers(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_futures_funding_rate_history():
    res = client.get_futures_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None


def test_get_contract_order_book_delivery():
    res = client.get_contract_order_book(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
    assert res is not None


def test_get_contract_kline_delivery():
    res = client.get_contract_kline(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
    assert res is not None


def test_get_contract_list_tickers_delivery():
    res = client.get_contract_list_tickers(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
    assert res is not None


def test_get_spot_all_currency_pairs():
    res = client.get_spot_all_currency_pairs()
    assert res is not None


def test_get_spot_order_book():
    res = client.get_spot_order_book(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_spot_kline():
    res = client.get_spot_kline(product_symbol="BTC-USDT-SPOT")
    assert res is not None


def test_get_spot_list_tickers():
    res = client.get_spot_list_tickers(product_symbol="BTC-USDT-SPOT")
    assert res is not None
