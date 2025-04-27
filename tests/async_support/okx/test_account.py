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
async def test_get_account_instruments(client):
    res = await client.get_account_instruments(instType="SPOT", product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_balance(client):
    res = await client.get_account_balance()
    assert res is not None


@pytest.mark.asyncio
async def test_get_positions(client):
    res = await client.get_positions(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_positions_history(client):
    res = await client.get_positions_history(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_position_risk(client):
    res = await client.get_position_risk()
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_bills(client):
    res = await client.get_account_bills(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_bills_archive(client):
    res = await client.get_account_bills_archive(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_post_account_bills_history_archive(client):
    res = await client.post_account_bills_history_archive(year="2025", quarter="Q1")
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_bills_history_archive(client):
    res = await client.get_account_bills_history_archive(year="2025", quarter="Q1")
    assert res is not None


@pytest.mark.asyncio
async def test_get_account_config(client):
    res = await client.get_account_config()
    assert res is not None


@pytest.mark.asyncio
async def test_set_position_mode(client):
    res = await client.set_position_mode(posMode="long_short_mode")
    assert res is not None


@pytest.mark.asyncio
async def test_get_max_order_size(client):
    res = await client.get_max_order_size(product_symbol="BTC-USDT-SPOT", tdMode="isolated")
    assert res is not None


@pytest.mark.asyncio
async def test_get_max_avail_size(client):
    res = await client.get_max_avail_size(product_symbol="BTC-USDT-SPOT", tdMode="cash")
    assert res is not None


@pytest.mark.asyncio
async def test_get_leverage(client):
    res = await client.get_leverage(product_symbol="BTC-USDT-SWAP", mgnMode="cross")
    assert res is not None


@pytest.mark.asyncio
async def test_get_adjust_leverage(client):
    res = await client.get_adjust_leverage(product_symbol="BTC-USDT-SWAP", instType="SWAP", mgnMode="cross", lever="3")
    assert res is not None


@pytest.mark.asyncio
async def test_get_max_loan(client):
    res = await client.get_max_loan(product_symbol="BTC-USDT-SPOT", mgnMode="cross", mgnCcy="USDT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_fee_rates(client):
    res = await client.get_fee_rates(product_symbol="BTC-USDT-SPOT", instType="SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_interest_accrued(client):
    res = await client.get_interest_accrued(product_symbol="BTC-USDT-SPOT")
    assert res is not None


@pytest.mark.asyncio
async def test_get_interest_rate(client):
    res = await client.get_interest_rate()
    assert res is not None


@pytest.mark.asyncio
async def test_set_greeks(client):
    res = await client.set_greeks(greeksType="PA")
    assert res is not None


@pytest.mark.asyncio
async def test_get_max_withdrawal(client):
    res = await client.get_max_withdrawal()
    assert res is not None


@pytest.mark.asyncio
async def test_get_interest_limits(client):
    res = await client.get_interest_limits()
    assert res is not None


@pytest.mark.asyncio
async def test_set_leverage(client):
    res = await client.set_leverage(lever="10", mgnMode="cross", product_symbol="BTC-USDT-SWAP")
    assert res is not None


@pytest.mark.asyncio
async def test_set_isolated_mode(client):
    res = await client.set_isolated_mode(type="CONTRACTS")
    assert res is not None
