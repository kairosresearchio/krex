import pytest
import pytest_asyncio
from krex.async_support.bitmex.client import Client


@pytest_asyncio.fixture
async def client():
    async with Client() as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_instrument_info(client):
    res = await client.get_instrument_info()
    assert res is not None


@pytest.mark.asyncio
async def test_get_instrument_info_with_symbol(client):
    res = await client.get_instrument_info(product_symbol="XBT-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_orderbook(client):
    res = await client.get_orderbook(product_symbol="XBT-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_trades(client):
    res = await client.get_trades(product_symbol="XBT-USDT-SWAP", count=10)
    assert res is not None


@pytest.mark.asyncio
async def test_get_ticker(client):
    res = await client.get_ticker(symbol="XBT-USDT-SWAP", binSize="1m", count=5)
    assert res is not None


@pytest.mark.asyncio
async def test_get_kline(client):
    res = await client.get_kline(symbol="XBT-USDT-SWAP", binSize="1m", count=5)
    assert res is not None


@pytest.mark.asyncio
async def test_get_funding(client):
    res = await client.get_funding(product_symbol="XBT-USDT-SWAP", count=10)
    assert res is not None
