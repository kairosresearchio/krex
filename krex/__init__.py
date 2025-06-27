"""
KREX - Kairos Research Exchange Library

A comprehensive library for cryptocurrency exchange interactions with both sync and async support.
Automatically handles Jupyter Notebook compatibility with nest_asyncio.
"""

# 自動處理 Jupyter 環境的 nest_asyncio
from .utils.jupyter_helper import auto_apply_nest_asyncio

# Import exchange client classes and create callable functions
from .bybit.client import Client as BybitClient
from .binance.client import Client as BinanceClient
from .okx.client import Client as OKXClient
from .bitmart.client import Client as BitmartClient
from .gateio.client import Client as GateioClient
from .hyperliquid.client import Client as HyperliquidClient


# 在導入時自動應用（如果需要的話）
auto_apply_nest_asyncio(verbose=False)


# Create callable functions for each exchange
def bybit(**kwargs):
    """Create a Bybit client instance."""
    return BybitClient(**kwargs)


def binance(**kwargs):
    """Create a Binance client instance."""
    return BinanceClient(**kwargs)


def okx(**kwargs):
    """Create an OKX client instance."""
    return OKXClient(**kwargs)


def bitmart(**kwargs):
    """Create a BitMart client instance."""
    return BitmartClient(**kwargs)


def gateio(**kwargs):
    """Create a Gate.io client instance."""
    return GateioClient(**kwargs)


def hyperliquid(**kwargs):
    """Create a Hyperliquid client instance."""
    return HyperliquidClient(**kwargs)


__all__ = [
    "bybit",
    "binance",
    "okx",
    "bitmart",
    "gateio",
    "hyperliquid",
]
