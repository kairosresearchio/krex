import asyncio
import pandas as pd
from krex.utils.decimal_utils import get_decimal_places
from krex.table.fetch import fetch_bybit, fetch_okx


async def bybit() -> pd.DataFrame:
    """
    Prepare the product table for the exchange.
    """
    loop = asyncio.get_running_loop()
    markets = await loop.run_in_executor(None, fetch_bybit)
    rows = []
    for symbol, info in markets.items():
        # our_symbol = symbol + "-SWAP"
        row = {
            "exchange": "Bybit",
            "exchange_symbol": symbol,
            "product_symbol": f"{symbol[:-4]}-{symbol[-4:]}-SWAP",
            "price_precision": get_decimal_places(float(info["price_precision"])),
            "size_precision": get_decimal_places(float(info["size_precision"])),
            "contract_value": float(info["contract_value"]),
            "min_size": float(info["min_size"]),
            "min_notional": info["min_notional"],
            "product_type": "SWAP",
        }
        rows.append(row)
    df = pd.DataFrame(rows)
    return df


async def okx() -> pd.DataFrame:
    """
    Prepare the product table for the exchange.
    """
    loop = asyncio.get_running_loop()
    markets = await loop.run_in_executor(None, fetch_okx)
    rows = []
    for symbol, info in markets.items():
        row = {
            "exchange": "OKX",
            "exchange_symbol": symbol,
            "product_symbol": symbol,
            "price_precision": get_decimal_places(float(info["price_precision"])),
            "size_precision": get_decimal_places(float(info["size_precision"])),
            "contract_value": float(info["contract_value"]),
            "min_size": float(info["min_size"]),
            "min_notional": info["min_notional"],
            "product_type": "SWAP",
        }
        rows.append(row)
    df = pd.DataFrame(rows)
    return df
