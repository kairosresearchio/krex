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
async def test_get_coin_info(client):
    res = await client.get_coin_info()
    assert res is not None


# @pytest.mark.asyncio
# async def test_get_sub_uid(client):
#     res = await client.get_sub_uid()
#     assert res is not None


@pytest.mark.asyncio
async def test_get_spot_asset_info(client):
    res = await client.get_spot_asset_info()
    assert res is not None


@pytest.mark.asyncio
async def test_get_coins_balance(client):
    res = await client.get_coins_balance(accountType="FUND")
    assert res is not None


@pytest.mark.asyncio
async def test_get_coin_balance(client):
    res = await client.get_coin_balance(accountType="FUND", coin="BTC")
    assert res is not None


@pytest.mark.asyncio
async def test_get_withdrawable_amount(client):
    res = await client.get_withdrawable_amount(coin="USDT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_internal_transfer_records(client):
    res = await client.get_internal_transfer_records()
    assert res is not None


@pytest.mark.asyncio
async def test_get_universal_transfer_records(client):
    res = await client.get_universal_transfer_records()
    assert res is not None


@pytest.mark.asyncio
async def test_get_deposit_records(client):
    res = await client.get_deposit_records()
    assert res is not None


@pytest.mark.asyncio
async def test_get_internal_deposit_records(client):
    res = await client.get_internal_deposit_records()
    assert res is not None


# @pytest.mark.asyncio
# async def test_get_master_deposit_address(client):
#     res = await client.get_master_deposit_address(coin="USDT")
#     assert res is not None


@pytest.mark.asyncio
async def test_get_withdrawal_records(client):
    res = await client.get_withdrawal_records()
    assert res is not None
