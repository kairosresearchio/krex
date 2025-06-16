import pytest
import pytest_asyncio
from krex.async_support.bybit.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=BYBIT_API_KEY,
        api_secret=BYBIT_API_SECRET,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_positions(client):
    res = await client.get_positions(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_closed_pnl(client):
    res = await client.get_closed_pnl()
    assert res is not None
