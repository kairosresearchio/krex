from typing import Dict
from krex.bybit._market_http import MarketHTTP
from krex.okx._public_http import PublicHTTP


def fetch_bybit() -> Dict[str, Dict[str, str]]:
    market_http = MarketHTTP()
    response = market_http.get_instruments_info(category="linear")

    if "result" not in response or "list" not in response["result"]:
        raise ValueError("Invalid response format from Bybit API")

    markets = {}
    for market in response["result"]["list"]:
        markets[market["symbol"]] = {
            "price_precision": market["priceFilter"]["minPrice"],
            "size_precision": market["priceFilter"]["tickSize"],
            "contract_value": market["leverageFilter"]["maxLeverage"],
            "min_size": market["lotSizeFilter"]["minOrderQty"],
            "min_notional": market["lotSizeFilter"].get("minNotionalValue", "0"),
        }

    return markets


def fetch_okx() -> Dict[str, Dict[str, str]]:
    public_http = PublicHTTP()
    response = public_http.get_instruments(instType="SWAP")

    if "data" not in response or not isinstance(response["data"], list):
        raise ValueError("Invalid response format from OKX API")

    markets = {}
    for market in response["data"]:
        markets[market["instId"]] = {
            "price_precision": market["tickSz"],
            "size_precision": market["lotSz"],
            "contract_value": market["ctVal"],
            "min_size": market["minSz"],
            "min_notional": market.get("minNotional", "0"),
        }
    return markets
