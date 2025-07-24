# Import exchange client classes and create callable functions
from .bybit.client import Client as BybitClient
from .binance.client import Client as BinanceClient
from .okx.client import Client as OKXClient
from .bitmart.client import Client as BitmartClient
from .gateio.client import Client as GateioClient
from .hyperliquid.client import Client as HyperliquidClient
from .bingx.client import Client as BingXClient
from .kucoin.client import Client as KuCoinClient
from .ascendex.client import Client as AscendexClient
from .bitmex.client import Client as BitmexClient
from .zoomex.client import Client as ZoomexClient


async def bybit(**kwargs):
    """Create and initialize a Bybit client instance."""
    client = BybitClient(**kwargs)
    await client.async_init()
    return client


async def binance(**kwargs):
    """Create and initialize a Binance client instance."""
    client = BinanceClient(**kwargs)
    await client.async_init()
    return client


async def okx(**kwargs):
    """Create and initialize an OKX client instance."""
    client = OKXClient(**kwargs)
    await client.async_init()
    return client


async def bitmart(**kwargs):
    """Create and initialize a BitMart client instance."""
    client = BitmartClient(**kwargs)
    await client.async_init()
    return client


async def gateio(**kwargs):
    """Create and initialize a Gate.io client instance."""
    client = GateioClient(**kwargs)
    await client.async_init()
    return client


async def hyperliquid(**kwargs):
    """Create and initialize a Hyperliquid client instance."""
    client = HyperliquidClient(**kwargs)
    await client.async_init()
    return client


async def bingx(**kwargs):
    """Create and initialize a BingX client instance."""
    client = BingXClient(**kwargs)
    await client.async_init()
    return client


async def kucoin(**kwargs):
    """Create and initialize a KuCoin client instance."""
    client = KuCoinClient(**kwargs)
    await client.async_init()
    return client


async def ascendex(**kwargs):
    """Create and initialize a AscendEX client instance."""
    client = AscendexClient(**kwargs)
    await client.async_init()
    return client


async def bitmex(**kwargs):
    """Create and initialize a BitMEX client instance."""
    client = BitmexClient(**kwargs)
    await client.async_init()
    return client


async def zoomex(**kwargs):
    """Create and initialize a Zoomex client instance."""
    client = ZoomexClient(**kwargs)
    await client.async_init()
    return client

__all__ = [
    "bybit",
    "binance",
    "okx",
    "bitmart",
    "gateio",
    "hyperliquid",
    "bingx",
    "kucoin",
    "ascendex",
    "bitmex",
    "zoomex",
]
