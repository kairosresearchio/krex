import pytest
import pytest_asyncio
from krex.async_support.bitmex.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=BITMEX_API_KEY,
        api_secret=BITMEX_API_SECRET,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_executions(client):
    res = await client.get_executions(product_symbol="XBT-USDT-SWAP", count=5)
    assert res is not None


@pytest.mark.asyncio
async def test_get_trade_history(client):
    res = await client.get_trade_history(product_symbol="XBT-USDT-SWAP", count=5)
    assert res is not None


@pytest.mark.asyncio
async def test_get_trading_volume(client):
    res = await client.get_trading_volume()
    assert res is not None
