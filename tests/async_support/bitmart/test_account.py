import pytest
import pytest_asyncio
from krex.async_support.bitmart.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

BITMART_API_KEY = os.getenv("BITMART_API_KEY")
BITMART_API_SECRET = os.getenv("BITMART_API_SECRET")
MEMO = os.getenv("BITMART_MEMO")


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=BITMART_API_KEY,
        api_secret=BITMART_API_SECRET,
        memo=MEMO,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_account_balance(client):
    res = await client.get_account_balance()
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_currencies(client):
    res = await client.get_account_currencies()
    assert res is not None


@pytest.mark.asyncio
async def test_get_spot_wallet(client):
    res = await client.get_spot_wallet()
    assert res is not None


@pytest.mark.asyncio
async def test_get_deposit_address(client):
    res = await client.get_deposit_address(currency="BTC")
    assert res is not None


@pytest.mark.asyncio
async def test_get_withdraw_charge(client):
    res = await client.get_withdraw_charge(currency="BTC")
    assert res is not None


@pytest.mark.asyncio
async def test_get_deposit_withdraw_history(client):
    res = await client.get_deposit_withdraw_history(currency="USDT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_deposit_withdraw_history_detail(client):
    res = await client.get_deposit_withdraw_history_detail(id="26695771")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_assets(client):
    res = await client.get_contract_assets()
    assert res is not None
