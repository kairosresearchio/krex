import pytest
import pytest_asyncio
from krex.async_support.okx.client import Client

OKX_API_KEY = "afef1997-a90a-4dd2-bc2e-c74b500bbb03"
OKX_API_SECRET = "186529BB2AAD75A6B88E63A7EC1D3179"
OKX_PASSPHRASE = "Aras1234@"


@pytest_asyncio.fixture
async def client():
    async with Client(
        api_key=OKX_API_KEY,
        api_secret=OKX_API_SECRET,
        passphrase=OKX_PASSPHRASE,
    ) as client_instance:
        yield client_instance


@pytest.mark.asyncio
async def test_get_public_instruments(client):
    res = await client.get_public_instruments(instType="SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_funding_rate(client):
    res = await client.get_funding_rate(product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_get_funding_rate_history(client):
    res = await client.get_funding_rate_history(product_symbol="BTC-USDT-SWAP")
    assert res is not None
