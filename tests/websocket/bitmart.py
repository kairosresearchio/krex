import os
import polars as pl
import pytest
from unittest.mock import AsyncMock, patch
from krex.websocket.data.market_data import MarketData

from dotenv import load_dotenv

load_dotenv()


async def initialize(shared_data: MarketData):
    from krex.async_support.bitmart.client import Client
    from krex.websocket.bitmart import BitmartPublicWsClient

    bitmart_client = Client(
        api_key=os.getenv("BITMART_APIKEY"),
        api_secret=os.getenv("BITMART_APISECRET"),
        memo=os.getenv("BITMART_MEMO"),
    )
    await bitmart_client.async_init()

    kline_df = await bitmart_client.get_contract_kline(
        product_symbol="ETH-USDT-SWAP",
        interval="1m",
        start_time=0,
        end_time=0,
    )
    await shared_data.update_kline_data("bitmart", "ETH-USDT-SWAP", kline_df)

    ws_client = await BitmartPublicWsClient.create(
        subscription={"action": "subscribe", "args": []},
        api_key=os.getenv("BITMART_APIKEY"),
        api_secret=os.getenv("BITMART_APISECRET"),
        memo=os.getenv("BITMART_MEMO"),
        slack_bot_name="GHOST",
        slack_channel_name="CRITICAL",
    )
    ws_client.market_data = shared_data
    return ws_client


@pytest.mark.asyncio
async def test_initialize_should_return_ws_client():
    data = MarketData()

    with (
        patch("krex.async_support.bitmart.client.Client") as mock_client_cls,
        patch("krex.websocket.bitmart.BitmartPublicWsClient.create", new_callable=AsyncMock) as mock_ws_create,
    ):
        mock_client = AsyncMock()
        mock_client.get_contract_kline.return_value = pl.DataFrame(
            {
                "datetime": [1672531200 * 1000],
                "open": [100],
                "high": [110],
                "low": [90],
                "close": [105],
                "volume": [1000],
            }
        ).with_columns([pl.col("datetime").cast(pl.Datetime).dt.cast_time_unit("ms")])
        mock_client_cls.return_value = mock_client

        mock_ws_client = AsyncMock()
        mock_ws_create.return_value = mock_ws_client

        ws_client = await initialize(data)

        assert ws_client is mock_ws_client
        mock_ws_create.assert_awaited_once()
        mock_client.get_contract_kline.assert_awaited_once()
