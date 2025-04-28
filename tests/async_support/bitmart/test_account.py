import pytest
import pytest_asyncio
from krex.async_support.bitmart.client import Client


BITMART_API_KEY = "613c8332848ff6b83aa915ae6270f2e842901036"
BITMART_API_SECRET = "66b82353bfee263185b36bdcaa244ee805c68aa87fd593addcd5124ff334ea3f"
MEMO = "trade"


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
