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
async def test_get_spot_exchange_info(client):
    res = await client.get_spot_exchange_info(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_futures_exchange_info(client):
    res = await client.get_futures_exchange_info()
    assert res is not None


@pytest.mark.asyncio
async def test_get_futures_ticker(client):
    res = await client.get_futures_ticker(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_futures_kline(client):
    res = await client.get_futures_kline(product_symbol="BTC-USDT-SWAP", interval="1m")
    assert res is not None


@pytest.mark.asyncio
async def test_get_futures_premium_index(client):
    res = await client.get_futures_premium_index(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_futures_funding_rate(client):
    res = await client.get_futures_funding_rate(product_symbol="BTC-USDT-SWAP")
    assert res is not None
