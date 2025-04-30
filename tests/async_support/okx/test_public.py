import pytest
import pytest_asyncio
from krex.async_support.okx.client import Client


@pytest_asyncio.fixture
async def client():
    async with Client() as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_public_instruments(client):
    res = await client.get_public_instruments(instType="SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_funding_rate(client):
    res = await client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_funding_rate_history(client):
    res = await client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None
