import pytest
import pytest_asyncio
from datetime import datetime, timedelta
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
async def test_get_spot_currencies(client):
    res = await client.get_spot_currencies()
    assert res is not None


@pytest.mark.asyncio
async def test_get_trading_pairs(client):
    res = await client.get_trading_pairs()
    assert res is not None


@pytest.mark.asyncio
async def test_get_trading_pairs_details(client):
    res = await client.get_trading_pairs_details()
    assert res is not None


@pytest.mark.asyncio
async def test_get_ticker_of_all_pairs(client):
    res = await client.get_ticker_of_all_pairs()
    assert res is not None


@pytest.mark.asyncio
async def test_get_ticker_of_a_pair(client):
    res = await client.get_ticker_of_a_pair(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_spot_kline(client):
    res = await client.get_spot_kline("BTC-USDT-SPOT", "5m")
    assert res is not None


@pytest.mark.asyncio
async def test_get_depth(client):
    res = await client.get_depth(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_contract_kline(client):
    start = int((datetime.now() - timedelta(days=1)).timestamp())
    end = int(datetime.now().timestamp())
    res = await client.get_contract_kline("BTC-USDT-SWAP", "5m", start, end)
    assert res is not None
