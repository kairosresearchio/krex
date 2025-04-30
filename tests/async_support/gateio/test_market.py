import pytest
import pytest_asyncio


from krex.async_support.gateio.client import Client


@pytest_asyncio.fixture
async def client():
    async with Client() as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_all_futures_contracts(client):
    res = await client.get_all_futures_contracts()
    assert res is not None


@pytest.mark.asyncio
async def test_get_a_single_futures_contract(client):
    res = await client.get_a_single_futures_contract(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_order_book_futures(client):
    res = await client.get_contract_order_book(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_kline_futures(client):
    res = await client.get_contract_kline(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_list_tickers_futures(client):
    res = await client.get_contract_list_tickers(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_futures_funding_rate_history(client):
    res = await client.get_futures_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_order_book_delivery(client):
    res = await client.get_contract_order_book(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_kline_delivery(client):
    res = await client.get_contract_kline(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_list_tickers_delivery(client):
    res = await client.get_contract_list_tickers(product_symbol="BTC-USDT-20250926-SWAP", path="delivery")
    assert res is not None


@pytest.mark.asyncio
async def test_get_spot_all_currency_pairs(client):
    res = await client.get_spot_all_currency_pairs()
    assert res is not None


@pytest.mark.asyncio
async def test_get_spot_order_book(client):
    res = await client.get_spot_order_book(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_spot_kline(client):
    res = await client.get_spot_kline(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_spot_list_tickers(client):
    res = await client.get_spot_list_tickers(product_symbol="BTC-USDT-SPOT")
    assert res is not None
