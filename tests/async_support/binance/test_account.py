import pytest
import pytest_asyncio
from krex.async_support.binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()


BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=BINANCE_API_KEY,
        api_secret=BINANCE_API_SECRET,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_account_balance(client):
    res = await client.get_account_balance()
    assert res is not None


@pytest.mark.asyncio
async def test_get_income_history(client):
    res = await client.get_income_history()
    assert res is not None
