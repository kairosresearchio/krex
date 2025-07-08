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
async def test_get_wallet_summary(client):
    res = await client.get_wallet_summary()
    assert res is not None
