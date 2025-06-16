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
async def test_get_wallet_balance(client):
    res = await client.get_wallet_balance()
    assert res is not None


@pytest.mark.asyncio
async def test_get_transferable_amount(client):
    res = await client.get_transferable_amount(coins=["BTC", "ETH"])
    assert res is not None


@pytest.mark.asyncio
async def test_get_borrow_history(client):
    res = await client.get_borrow_history()
    assert res is not None


@pytest.mark.asyncio
async def test_get_collateral_info(client):
    res = await client.get_collateral_info()
    assert res is not None


@pytest.mark.asyncio
async def test_get_fee_rates(client):
    res = await client.get_fee_rates()
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_info(client):
    res = await client.get_account_info()
    assert res is not None


@pytest.mark.asyncio
async def test_get_transaction_log(client):
    res = await client.get_transaction_log()
    assert res is not None
