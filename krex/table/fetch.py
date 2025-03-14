from typing import Dict
from krex.bybit._market_http import MarketHTTP
from krex.okx._public_http import PublicHTTP
from dataclasses import dataclass, asdict
import pandas as pd
import re


@dataclass
class MarketInfo:
    exchange: str
    exchange_symbol: str
    product_symbol: str
    product_type: str
    price_precision: str
    size_precision: str
    min_size: str
    min_notional: str = "0"
    
    # contract
    size_per_contract: str = "1"

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


def strip_number(s: str) -> str:
    return re.sub(r'^\d+', '', s)

async def bybit() -> Dict[str, Dict[str, str]]:
    market_http = MarketHTTP()
    
    markets = []
    
    response = market_http.get_instruments_info(category="linear")
    for market in response["result"]["list"]:
        markets.append(MarketInfo(
            exchange="bybit",
            exchange_symbol=market["symbol"],
            product_symbol=f"{strip_number(market['symbol'][:-4])}-{market['symbol'][-4:]}-SWAP",
            product_type="SWAP",
            price_precision=market["priceFilter"]["tickSize"],
            size_precision=market["lotSizeFilter"]["qtyStep"],
            min_size=market["lotSizeFilter"]["minOrderQty"],
            min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
        ))
    
    response = market_http.get_instruments_info(category="inverse")
    for market in response["result"]["list"]:
        markets.append(MarketInfo(
            exchange="bybit",
            exchange_symbol=market["symbol"],
            product_symbol=f"{strip_number(market['symbol'][:-4])}-{market['symbol'][-4:]}-SWAP",
            product_type="SWAP",
            price_precision=market["priceFilter"]["tickSize"],
            size_precision=market["lotSizeFilter"]["qtyStep"],
            min_size=market["lotSizeFilter"]["minOrderQty"],
            min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
        ))
    
    response = market_http.get_instruments_info(category="spot")
    for market in response["result"]["list"]:
        markets.append(MarketInfo(
            exchange="bybit",
            exchange_symbol=market["symbol"],
            product_symbol=f"{market['symbol'][:-4]}-{market['symbol'][-4:]}-SPOT",
            product_type="SPOT",
            price_precision=market["priceFilter"]["tickSize"],
            size_precision=market["lotSizeFilter"]["basePrecision"],
            min_size=market["lotSizeFilter"]["minOrderQty"],
            min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
        ))
    markets = [market.to_dict() for market in markets]
    return pd.DataFrame(markets)


async def okx() -> Dict[str, Dict[str, str]]:
    public_http = PublicHTTP()
    
    markets = []
    
    response = public_http.get_instruments(instType="SWAP")
    for market in response["data"]:
        markets.append(MarketInfo(
            exchange="okx",
            exchange_symbol=market["instId"],
            product_symbol=strip_number(market["instId"]),
            product_type=market["instType"],
            price_precision=market["tickSz"],
            size_precision=market["lotSz"],
            min_size=market["minSz"],
            size_per_contract=market["ctVal"]
        ))
    
    response = public_http.get_instruments(instType="SPOT")
    for market in response["data"]:
        markets.append(MarketInfo(
            exchange="okx",
            exchange_symbol=market["instId"],
            product_symbol=market["instId"] + "-SPOT",
            product_type=market["instType"],
            price_precision=market["tickSz"],
            size_precision=market["lotSz"],
            min_size=market["minSz"],
            size_per_contract=market["ctVal"]
        ))
    
    markets = [market.to_dict() for market in markets]
    return pd.DataFrame(markets)
