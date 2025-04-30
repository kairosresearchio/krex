import pytest
import pytest_asyncio
from krex.async_support.okx.client import Client


@pytest_asyncio.fixture
async def client():
    async with Client() as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_candles_ticks(client):
    res = await client.get_candles_ticks(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_orderbook(client):
    res = await client.get_orderbook(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_tickers(client):
    res = await client.get_tickers(instType="SPOT")
    assert res is not None
