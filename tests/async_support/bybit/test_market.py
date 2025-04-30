import pytest
import pytest_asyncio
from krex.async_support.bybit.client import Client


@pytest_asyncio.fixture
async def client():
    async with Client() as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_instruments_info(client):
    res = await client.get_instruments_info(category="spot")
    assert res is not None


@pytest.mark.asyncio
async def test_get_kline(client):
    res = await client.get_kline(
        product_symbol="BTC-USDT-SPOT",
        interval="1m",
    )
    assert res is not None


@pytest.mark.asyncio
async def test_get_orderbook(client):
    res = await client.get_orderbook(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_tickers(client):
    res = await client.get_tickers()
    assert res is not None


@pytest.mark.asyncio
async def test_get_funding_rate_history(client):
    res = await client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None
