import re
import polars as pl
from typing import Dict
from dataclasses import dataclass, asdict
from ...utils.decimal_utils import reverse_decimal_places
from ...utils.common import Common


@dataclass
class MarketInfo:
    exchange: str
    exchange_symbol: str
    product_symbol: str
    product_type: str
    price_precision: str
    size_precision: str
    min_size: str
    base_currency: str = ""
    quote_currency: str = ""
    min_notional: str = "0"

    # contract
    size_per_contract: str = "1"

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


def strip_number(s: str) -> str:
    return re.sub(r"^\d+", "", s)


def clean_symbol(symbol: str) -> str:
    return re.sub(r"[$_]", "", symbol)


def format_product_symbol(symbol: str) -> str:
    """
    - BTCUSDT-04APR25 → BTC-USDT-04APR25-SWAP
    - ETH-25APR25 → ETH-25APR25-SWAP
    - AAVEUSD → AAVE-USD
    - ETHUSDH25 → ETH-USD-H25
    """
    match = re.match(r"([A-Z]+)(USD[T]?)-(\d+[A-Z]{3}\d{2})$", symbol)
    if match:
        base, quote, date = match.groups()
        return f"{base}-{quote}-{date}-SWAP"

    # ETH-25APR25 --> ETH-25APR25-SWAP
    match = re.match(r"([A-Z]+)-(\d+[A-Z]{3}\d{2})$", symbol)
    if match:
        base, date = match.groups()
        return f"{base}-{date}-SWAP"

    # ETHUSDH25 --> ETH-USD-H25-SWAP
    match = re.match(r"([A-Z]+)(USD[T]?)([HMU]\d{2})$", symbol)
    if match:
        base, quote, date = match.groups()
        return f"{base}-{quote}-{date}-SWAP"

    # AAVEUSD --> AAVE-USD-SWAP
    match = re.match(r"([A-Z]+)(USD[T]?)$", symbol)
    if match:
        base, quote = match.groups()
        return f"{base}-{quote}-SWAP"

    quote_currencies = {"USDT", "USDC", "PERP", "USD"}

    matched_quote = next((quote for quote in quote_currencies if symbol.endswith(quote)), None)

    if matched_quote:
        base = symbol[: -len(matched_quote)]
        return f"{base}-{matched_quote}-SWAP"

    return f"{symbol}-SWAP"


# async def bybit() -> Dict[str, Dict[str, str]]:
#     from ..bybit._market_http import MarketHTTP

#     market_http = MarketHTTP()

#     markets = []

#     response = await market_http.get_instruments_info(category="linear")
#     for market in response["result"]["list"]:
#         markets.append(
#             MarketInfo(
#                 exchange=Common.BYBIT,
#                 exchange_symbol=market["symbol"],
#                 product_symbol=format_product_symbol(strip_number(market["symbol"])),
#                 product_type="linear",
#                 base_currency=strip_number(market["baseCoin"]),
#                 quote_currency=market["quoteCoin"],
#                 price_precision=market["priceFilter"]["tickSize"],
#                 size_precision=market["lotSizeFilter"]["qtyStep"],
#                 min_size=market["lotSizeFilter"]["minOrderQty"],
#                 min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
#             )
#         )

#     response = await market_http.get_instruments_info(category="inverse")
#     for market in response["result"]["list"]:
#         markets.append(
#             MarketInfo(
#                 exchange=Common.BYBIT,
#                 exchange_symbol=market["symbol"],
#                 product_symbol=format_product_symbol(market["symbol"]),
#                 product_type="inverse",
#                 base_currency=strip_number(market["baseCoin"]),
#                 quote_currency=market["quoteCoin"],
#                 price_precision=market["priceFilter"]["tickSize"],
#                 size_precision=market["lotSizeFilter"]["qtyStep"],
#                 min_size=market["lotSizeFilter"]["minOrderQty"],
#             )
#         )

#     response = await market_http.get_instruments_info(category="spot")
#     for market in response["result"]["list"]:
#         if not market["symbol"].endswith(("USDT", "USDC")):
#             continue
#         markets.append(
#             MarketInfo(
#                 exchange=Common.BYBIT,
#                 exchange_symbol=market["symbol"],
#                 product_symbol=f"{market['symbol'][:-4]}-{market['symbol'][-4:]}-SPOT",
#                 product_type="spot",
#                 base_currency=strip_number(market["baseCoin"]),
#                 quote_currency=market["quoteCoin"],
#                 price_precision=market["priceFilter"]["tickSize"],
#                 size_precision=market["lotSizeFilter"]["basePrecision"],
#                 min_size=market["lotSizeFilter"]["minOrderQty"],
#                 min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
#             )
#         )
#     markets = [market.to_dict() for market in markets]
#     return pd.DataFrame(markets)


# async def okx() -> Dict[str, Dict[str, str]]:
#     from ..okx._public_http import PublicHTTP

#     public_http = PublicHTTP()

#     markets = []

#     response = await public_http.get_instruments(instType="SWAP")
#     for market in response["data"]:
#         markets.append(
#             MarketInfo(
#                 exchange=Common.OKX,
#                 exchange_symbol=market["instId"],
#                 product_symbol=strip_number(market["instId"]),
#                 product_type=market["instType"],
#                 base_currency=strip_number(market["baseCcy"]),
#                 quote_currency=market["quoteCcy"],
#                 price_precision=market["tickSz"],
#                 size_precision=market["lotSz"],
#                 min_size=market["minSz"],
#                 size_per_contract=market["ctVal"],
#             )
#         )

#     response = await public_http.get_instruments(instType="SPOT")
#     for market in response["data"]:
#         if not market["instId"].endswith(("USDT", "USDC")):
#             continue
#         markets.append(
#             MarketInfo(
#                 exchange=Common.OKX,
#                 exchange_symbol=market["instId"],
#                 product_symbol=market["instId"] + "-SPOT",
#                 product_type=market["instType"],
#                 base_currency=strip_number(market["baseCcy"]),
#                 quote_currency=market["quoteCcy"],
#                 price_precision=market["tickSz"],
#                 size_precision=market["lotSz"],
#                 min_size=market["minSz"],
#             )
#         )

#     markets = [market.to_dict() for market in markets]
#     return pd.DataFrame(markets)


async def bitmart() -> pl.DataFrame:
    from ..bitmart._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    quote_currencies = {"USDT", "USDC", "USD"}

    df_swap = await market_http.get_contracts_details()
    for market in df_swap.iter_rows(named=True):
        matched_quote = next(
            (quote for quote in quote_currencies if market["symbol"].endswith(quote)),
            None,
        )

        if matched_quote:
            base = market["symbol"][: -len(matched_quote)]
            product_symbol = f"{base}-{matched_quote}-SWAP"
        else:
            product_symbol = f"{market['symbol']}-SWAP"

        markets.append(
            MarketInfo(
                exchange=Common.BITMART,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="SWAP",
                base_currency=strip_number(market["base_currency"]),
                quote_currency=market["quote_currency"],
                price_precision=market["price_precision"],
                size_precision=market["vol_precision"],
                min_size=market["min_volume"],
                size_per_contract=market["contract_size"],
            )
        )

    df_spot = await market_http.get_trading_pairs_details()
    for market in df_spot.iter_rows(named=True):
        matched_quote = next(
            (quote for quote in quote_currencies if market["symbol"].endswith(quote)),
            None,
        )

        if matched_quote:
            base = clean_symbol(market["symbol"][: -len(matched_quote)])
            product_symbol = f"{base}-{matched_quote}-SPOT"
        else:
            product_symbol = f"{clean_symbol(market['symbol'])}-SPOT"

        markets.append(
            MarketInfo(
                exchange=Common.BITMART,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="SPOT",
                base_currency=strip_number(market["base_currency"]),
                quote_currency=market["quote_currency"],
                price_precision=reverse_decimal_places(market["price_max_precision"]),
                size_precision=market["quote_increment"],
                min_size=market["base_min_size"],
                min_notional=market["min_buy_amount"],
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)
