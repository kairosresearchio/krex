import asyncio
import polars as pl
from typing import Dict, Any

from ..models.order import TradeStatus
from ..models.position import PositionInfo
from ..models.ticker import BookTicker
from ..models.balance import BalanceInfo


class MarketData:
    _instance = None
    _lock = asyncio.Lock()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MarketData, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        self._initialized = False
        self._data_lock = asyncio.Lock()
        self._depth_data = {}
        self._kline_data = {}
        self._position_data = {}
        self._trade_data = {}
        self._balance_data = {}

    async def update_depth_data(self, exchange: str, symbol: str, data: BookTicker) -> None:
        async with self._data_lock:
            self._depth_data.setdefault(exchange, {})[symbol] = data

    async def get_depth_data(self, exchange: str, symbol: str) -> Any:
        async with self._data_lock:
            return self._depth_data.get(exchange, {}).get(symbol)

    async def get_all_depth_data(self) -> Dict[str, Any]:
        async with self._data_lock:
            return self._depth_data.copy()

    async def update_kline_data(self, exchange: str, symbol: str, data: pl.DataFrame) -> None:
        async with self._data_lock:
            self._kline_data.setdefault(exchange, {})
            if symbol in self._kline_data[exchange]:
                existing_df = self._kline_data[exchange][symbol]
                combined_df = pl.concat([existing_df, data])
            else:
                combined_df = data

            combined_df = combined_df.sort("datetime")
            combined_df = combined_df.unique(subset=["datetime"], keep="last")
            if combined_df.height > 1000:
                combined_df = combined_df.slice(-1000, 1000)

            self._kline_data[exchange][symbol] = combined_df

    async def get_kline_data(self, exchange: str, symbol: str) -> Any:
        async with self._data_lock:
            return self._kline_data.get(exchange, {}).get(symbol)

    async def get_all_kline_data(self) -> Dict[str, Any]:
        async with self._data_lock:
            return self._kline_data.copy()

    async def update_position(self, exchange: str, symbol: str, data: PositionInfo) -> None:
        async with self._data_lock:
            self._position_data.setdefault(exchange, {})[symbol] = data

    async def get_position(self, symbol: str) -> Any:
        async with self._data_lock:
            return self._position_data.get(symbol)

    async def get_all_positions(self) -> Dict[str, Any]:
        async with self._data_lock:
            return self._position_data.copy()

    async def update_trade_status(self, exchange: str, symbol: str, data: TradeStatus) -> None:
        async with self._data_lock:
            self._trade_data.setdefault(exchange, {})[symbol] = data

    async def get_trade_status(self, order_id: str) -> Any:
        async with self._data_lock:
            return self._trade_data.get(order_id)

    async def get_all_trade_statuses(self) -> Dict[str, Any]:
        async with self._data_lock:
            return self._trade_data.copy()

    async def update_balance(self, exchange: str, symbol: str, data: BalanceInfo) -> None:
        async with self._data_lock:
            self._balance_data.setdefault(exchange, {})[symbol] = data

    async def get_balance(self, symbol: str) -> Any:
        async with self._data_lock:
            return self._balance_data.get(symbol)

    async def get_all_balances(self) -> Dict[str, Any]:
        async with self._data_lock:
            return self._balance_data.copy()
