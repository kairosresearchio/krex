import pytest
import pytest_asyncio
from krex.async_support.binance.client import Client

BINANCE_APIKEY = "ovqxr2nXR50oeKo47CVKZTZ7ZmaCY3y1q7iAEOfsDXliAv52koJIcHEtlHDH30AU"
BINANCE_APISECRET = "sZ4nwX3owfZNDu4qBu0Y4H8zbic4E6FLtkbbNytV5Z6S77ZTiCgGxgYxHVitq4GQ"


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=BINANCE_APIKEY,
        api_secret=BINANCE_APISECRET,
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
