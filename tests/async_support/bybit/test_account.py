import pytest
import pytest_asyncio
from krex.async_support.bybit.client import Client

BYBIT_API_KEY = "VLOpq0qMKPNWhMbKVH"
BYBIT_API_SECRET = "Q3OKhzHiVSOYE2tF8ns2My4mQU7B8d5MnbOt"


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
