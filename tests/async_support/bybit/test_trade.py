import pytest
import pytest_asyncio
from krex.async_support.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_open_orders(client):
    res = await client.get_open_orders(category="spot")
    assert res is not None


@pytest.mark.asyncio
async def test_get_order_history(client):
    res = await client.get_order_history()
    assert res is not None


@pytest.mark.asyncio
async def test_get_execution_list(client):
    res = await client.get_execution_list()
    assert res is not None


@pytest.mark.asyncio
async def test_get_borrow_quota(client):
    res = await client.get_borrow_quota(product_symbol="BTC-USDT-SWAP", side="Buy")
    assert res is not None


@pytest.mark.asyncio
async def test_get_vip_margin_data(client):
    res = await client.get_vip_margin_data()
    assert res is not None


@pytest.mark.asyncio
async def test_get_collateral(client):
    res = await client.get_collateral()
    assert res is not None


@pytest.mark.asyncio
async def test_get_historical_interest_rate(client):
    res = await client.get_historical_interest_rate(currency="USDT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_status_and_leverage(client):
    res = await client.get_status_and_leverage()
    assert res is not None
