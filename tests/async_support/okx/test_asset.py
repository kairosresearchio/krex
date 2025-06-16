import pytest
import pytest_asyncio
from krex.async_support.okx.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

OKX_API_KEY = os.getenv("OKX_API_KEY")
OKX_API_SECRET = os.getenv("OKX_API_SECRET")
OKX_PASSPHRASE = os.getenv("OKX_PASSPHRASE")


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=OKX_API_KEY,
        api_secret=OKX_API_SECRET,
        passphrase=OKX_PASSPHRASE,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_currencies(client):
    res = await client.get_currencies()
    assert res is not None


@pytest.mark.asyncio
async def test_get_balances(client):
    res = await client.get_balances()
    assert res is not None


@pytest.mark.asyncio
async def test_get_asset_valuation(client):
    res = await client.get_asset_valuation()
    assert res is not None


@pytest.mark.asyncio
async def test_get_bills(client):
    res = await client.get_bills()
    assert res is not None


@pytest.mark.asyncio
async def test_get_deposit_address(client):
    res = await client.get_deposit_address(ccy="BTC")
    assert res is not None


@pytest.mark.asyncio
async def test_get_deposit_history(client):
    res = await client.get_deposit_history()
    assert res is not None


@pytest.mark.asyncio
async def test_get_withdrawal_history(client):
    res = await client.get_withdrawal_history()
    assert res is not None


@pytest.mark.asyncio
async def test_get_exchange_list(client):
    res = await client.get_exchange_list()
    assert res is not None


@pytest.mark.asyncio
async def test_post_monthly_statement(client):
    res = await client.post_monthly_statement(month="Mar")
    assert res is not None


@pytest.mark.asyncio
async def test_get_monthly_statement(client):
    res = await client.get_monthly_statement(month="Mar")
    assert res is not None


@pytest.mark.asyncio
async def test_get_convert_currencies(client):
    res = await client.get_convert_currencies()
    assert res is not None
