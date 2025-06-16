import re
import polars as pl
from typing import Dict
from dataclasses import dataclass, asdict
from ..utils.decimal_utils import reverse_decimal_places
from ..utils.common import Common
from ..utils.common_dataframe import to_dataframe


@dataclass
class MarketInfo:
    exchange: str
    exchange_symbol: str
    product_symbol: str
    product_type: str
    exchange_type: str
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
    - BTCUSDT → BTC-USDT-SWAP
    - BTCUSDT-04APR25 → BTC-USDT-04APR25-FUTURES
    - ETH-25APR25 → ETH-25APR25-FUTURES
    - AAVEUSD → AAVE-USD
    - ETHUSDH25 → ETH-USD-H25
    """
    match = re.match(r"([A-Z]+)(USD[T]?)\-([0-9]{2}[A-Z]{3}[0-9]{2})$", symbol)
    if match:
        base, quote, date = match.groups()
        return f"{base}-{quote}-{date}-FUTURES"

    # ETH-25APR25 --> ETH-25APR25-FUTURES
    match = re.match(r"([A-Z]+)-(\d+[A-Z]{3}\d{2})$", symbol)
    if match:
        base, date = match.groups()
        return f"{base}-{date}-FUTURES"

    # ETHUSDH25 --> ETH-USD-H25-FUTURES
    match = re.match(r"([A-Z]+)(USD[T]?)([HMUZ]\d{2})$", symbol)
    if match:
        base, quote, date = match.groups()
        return f"{base}-{quote}-{date}-FUTURES"

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


async def bybit() -> pl.DataFrame:
    from ..bybit._market_http import MarketHTTP

    market_http = MarketHTTP()

    markets = []

    res_linear = market_http.get_instruments_info(category="linear")
    df_linear = to_dataframe(res_linear["result"]["list"]) if "list" in res_linear.get("result", {}) else pl.DataFrame()
    for market in df_linear.iter_rows(named=True):
        if market["contractType"] == "LinearFutures":
            product_type = "futures"
        else:
            product_type = "swap"
        markets.append(
            MarketInfo(
                exchange=Common.BYBIT,
                exchange_symbol=market["symbol"],
                product_symbol=format_product_symbol(strip_number(market["symbol"])),
                product_type=product_type,
                exchange_type="linear",
                base_currency=strip_number(market["baseCoin"]),
                quote_currency=market["quoteCoin"],
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["qtyStep"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
                min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
            )
        )

    res_inverse = market_http.get_instruments_info(category="inverse")
    df_inverse = (
        to_dataframe(res_inverse["result"]["list"]) if "list" in res_inverse.get("result", {}) else pl.DataFrame()
    )
    for market in df_inverse.iter_rows(named=True):
        if market["contractType"] == "InverseFutures":
            product_type = "futures"
        else:
            product_type = "swap"
        markets.append(
            MarketInfo(
                exchange=Common.BYBIT,
                exchange_symbol=market["symbol"],
                product_symbol=format_product_symbol(market["symbol"]),
                product_type=product_type,
                exchange_type="inverse",
                base_currency=strip_number(market["baseCoin"]),
                quote_currency=market["quoteCoin"],
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["qtyStep"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
            )
        )

    res_spot = market_http.get_instruments_info(category="spot")
    df_spot = to_dataframe(res_spot["result"]["list"]) if "list" in res_spot.get("result", {}) else pl.DataFrame()
    for market in df_spot.iter_rows(named=True):
        if not market["symbol"].endswith(("USDT", "USDC")):
            continue
        markets.append(
            MarketInfo(
                exchange=Common.BYBIT,
                exchange_symbol=market["symbol"],
                product_symbol=f"{market['symbol'][:-4]}-{market['symbol'][-4:]}-SPOT",
                product_type="spot",
                exchange_type="spot",
                base_currency=strip_number(market["baseCoin"]),
                quote_currency=market["quoteCoin"],
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["basePrecision"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
                min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
            )
        )
    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def okx() -> pl.DataFrame:
    from ..okx._public_http import PublicHTTP

    public_http = PublicHTTP()

    markets = []

    res_swap = public_http.get_public_instruments(instType="SWAP")
    df_swap = to_dataframe(res_swap["data"]) if "data" in res_swap else pl.DataFrame()
    for market in df_swap.iter_rows(named=True):
        base = strip_number(market["baseCcy"])
        quote = market["quoteCcy"]

        if not base or not quote:
            parts = market["instId"].split("-")
            if len(parts) >= 2:
                base, quote = parts[0], parts[1]
        markets.append(
            MarketInfo(
                exchange=Common.OKX,
                exchange_symbol=market["instId"],
                product_symbol=strip_number(market["instId"]),
                product_type="swap",
                exchange_type=market["instType"],
                base_currency=base,
                quote_currency=quote,
                price_precision=market["tickSz"],
                size_precision=market["lotSz"],
                min_size=market["minSz"],
                size_per_contract=market["ctVal"],
            )
        )

    res_spot = public_http.get_public_instruments(instType="SPOT")
    df_spot = to_dataframe(res_spot["data"]) if "data" in res_spot else pl.DataFrame()
    for market in df_spot.iter_rows(named=True):
        if not market["instId"].endswith(("USDT", "USDC", "USD")):
            continue
        markets.append(
            MarketInfo(
                exchange=Common.OKX,
                exchange_symbol=market["instId"],
                product_symbol=market["instId"] + "-SPOT",
                product_type="spot",
                exchange_type=market["instType"],
                base_currency=strip_number(market["baseCcy"]),
                quote_currency=market["quoteCcy"],
                price_precision=market["tickSz"],
                size_precision=market["lotSz"],
                min_size=market["minSz"],
            )
        )

    res_futures = public_http.get_public_instruments(instType="FUTURES")
    df_futures = to_dataframe(res_futures["data"]) if "data" in res_futures else pl.DataFrame()
    for market in df_futures.iter_rows(named=True):
        base = strip_number(market["baseCcy"])
        quote = market["quoteCcy"]

        if not base or not quote:
            parts = market["instId"].split("-")
            if len(parts) >= 2:
                base, quote = parts[0], parts[1]

        markets.append(
            MarketInfo(
                exchange=Common.OKX,
                exchange_symbol=market["instId"],
                product_symbol=strip_number(market["instId"]),
                product_type="futures",
                exchange_type=market["instType"],
                base_currency=base,
                quote_currency=quote,
                price_precision=market["tickSz"],
                size_precision=market["lotSz"],
                min_size=market["minSz"],
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def bitmart() -> pl.DataFrame:
    from ..bitmart._market_http import MarketHTTP

    market_http = MarketHTTP()

    markets = []
    quote_currencies = {"USDT", "USDC", "USD"}

    res_swap = market_http.get_contracts_details()
    df_swap = to_dataframe(res_swap.get("data", {}).get("symbols", []))
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
                product_type="swap",
                exchange_type="swap",
                base_currency=strip_number(market["base_currency"]),
                quote_currency=market["quote_currency"],
                price_precision=market["price_precision"],
                size_precision=market["vol_precision"],
                min_size=market["min_volume"],
                size_per_contract=market["contract_size"],
            )
        )

    res_spot = market_http.get_trading_pairs_details()
    df_spot = to_dataframe(res_spot.get("data", {}).get("symbols", []))
    for market in df_spot.iter_rows(named=True):
        if not market["symbol"].endswith(("USDT", "USDC", "USD")):
            continue

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
                product_type="spot",
                exchange_type="spot",
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


async def gateio() -> pl.DataFrame:
    from ..gateio._market_http import MarketHTTP

    market_http = MarketHTTP()

    markets = []
    quote_currencies = {"USDT", "USDC", "USD"}

    res_futures = market_http.get_all_futures_contracts()
    df_futures = to_dataframe(res_futures)
    for market in df_futures.iter_rows(named=True):
        matched_quote = next(
            (quote for quote in quote_currencies if market["name"].endswith(quote)),
            None,
        )

        if matched_quote:
            base = clean_symbol(market["name"][: -len(matched_quote)])
            product_symbol = f"{base}-{matched_quote}-SWAP"
        else:
            product_symbol = f"{clean_symbol(market['name'])}-SWAP"

        parts = market["name"].split("_")
        if len(parts) >= 2:
            base, quote = parts[0], parts[1]

        markets.append(
            MarketInfo(
                exchange=Common.GATEIO,
                exchange_symbol=market["name"],
                product_symbol=product_symbol,
                product_type="swap",
                exchange_type="futures",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["order_price_round"],
                size_precision=str(market["order_size_min"]),
                min_size=str(market["order_size_min"]),
                size_per_contract=market["quanto_multiplier"],
            )
        )

    res_delivery = market_http.get_all_delivery_contracts()
    df_deliver = to_dataframe(res_delivery)
    for market in df_deliver.iter_rows(named=True):
        matched_quote = next(
            (quote for quote in quote_currencies if market["name"].split("_")[1].endswith(quote)),
            None,
        )

        if matched_quote:
            base = clean_symbol(market["name"].split("_")[0])
            product_symbol = f"{base}-{matched_quote}-{market['name'].split('_')[2]}-SWAP"
        else:
            product_symbol = f"{clean_symbol(market['name'])}-SWAP"

        parts = market["name"].split("_")
        if len(parts) >= 2:
            base, quote = parts[0], parts[1]

        markets.append(
            MarketInfo(
                exchange=Common.GATEIO,
                exchange_symbol=market["name"],
                product_symbol=product_symbol,
                product_type="futures",
                exchange_type="delivery",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["order_price_round"],
                size_precision=str(market["order_size_min"]),
                min_size=str(market["order_size_min"]),
                size_per_contract=market["quanto_multiplier"],
            )
        )

    res_spot = market_http.get_spot_all_currency_pairs()
    df_spot = to_dataframe(res_spot)
    for market in df_spot.iter_rows(named=True):
        if not market["id"].endswith(("USDT", "USDC", "USD")):
            continue
        markets.append(
            MarketInfo(
                exchange=Common.GATEIO,
                exchange_symbol=market["id"],
                product_symbol=f"{market['base']}-{market['quote']}-SPOT",
                product_type="spot",
                exchange_type="spot",
                base_currency=market["base"],
                quote_currency=market["quote"],
                price_precision=reverse_decimal_places(market["precision"]),
                size_precision=reverse_decimal_places(market["amount_precision"]),
                min_size=market["min_base_amount"],
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def binance() -> pl.DataFrame:
    from ..binance._market_http import MarketHTTP

    market_http = MarketHTTP()

    markets = []
    quote_currencies = {"USDT", "USDC", "USD"}

    res_spot = market_http.get_spot_exchange_info()
    df_spot = to_dataframe(res_spot.get("symbols", []))
    for market in df_spot.iter_rows(named=True):
        if not market["symbol"].endswith(("USDT", "USDC", "USD")):
            continue

        matched_quote = next(
            (quote for quote in quote_currencies if market["symbol"].endswith(quote)),
            None,
        )

        if matched_quote:
            product_symbol = clean_symbol(f"{market['baseAsset']}-{market['quoteAsset']}-SPOT")

        price_filter = next((f for f in market["filters"] if f["filterType"] == "PRICE_FILTER"), {})
        lot_size_filter = next((f for f in market["filters"] if f["filterType"] == "LOT_SIZE"), {})
        min_notional_filter = next((f for f in market["filters"] if f["filterType"] == "MIN_NOTIONAL"), {})

        markets.append(
            MarketInfo(
                exchange=Common.BINANCE,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=market["baseAsset"],
                quote_currency=market["quoteAsset"],
                price_precision=price_filter.get("tickSize", "0"),
                size_precision=lot_size_filter.get("stepSize", "0"),
                min_size=lot_size_filter.get("minQty", "0"),
                min_notional=min_notional_filter.get("notional", "0"),
            )
        )

    res_futures = market_http.get_futures_exchange_info()
    df_futures = to_dataframe(res_futures.get("symbols", []))
    for market in df_futures.iter_rows(named=True):
        if not market["symbol"].endswith(("USDT", "USDC", "USD", "BUSD")):
            continue

        base = strip_number(market["baseAsset"])
        quote = market["quoteAsset"]
        product_symbol = f"{base}-{quote}-SWAP"

        price_filter = next((f for f in market["filters"] if f["filterType"] == "PRICE_FILTER"), {})
        lot_size_filter = next((f for f in market["filters"] if f["filterType"] == "LOT_SIZE"), {})
        min_notional_filter = next((f for f in market["filters"] if f["filterType"] == "MIN_NOTIONAL"), {})
        markets.append(
            MarketInfo(
                exchange=Common.BINANCE,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="swap",
                exchange_type=market["contractType"],
                base_currency=base,
                quote_currency=quote,
                price_precision=price_filter.get("tickSize", "0"),
                size_precision=lot_size_filter.get("stepSize", "0"),
                min_size=lot_size_filter.get("minQty", "0"),
                min_notional=min_notional_filter.get("notional", "0"),
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def hyperliquid() -> pl.DataFrame:  # TODO: need to be checked
    from ..hyperliquid._market_http import MarketHTTP

    market_http = MarketHTTP()

    markets = []

    res_perpetual = market_http.meta()
    df_perpetual = to_dataframe(res_perpetual.get("universe", []))

    for market in df_perpetual.iter_rows(named=True):
        coin = market["name"]
        tick = str(reverse_decimal_places(market["szDecimals"]))
        markets.append(
            MarketInfo(
                exchange=Common.HYPERLIQUID,
                exchange_symbol=coin,
                product_symbol=f"{coin}-USDC-SWAP",
                product_type="swap",
                exchange_type="perpetual",
                base_currency=coin,
                quote_currency="USDC",
                price_precision=tick,
                size_precision=tick,
                min_size=tick,
                size_per_contract="1",
            )
        )

    res_spot = market_http.spot_meta()
    df_tokens = to_dataframe(res_spot.get("tokens", []))
    df_spot = to_dataframe(res_spot.get("universe", []))

    for market in df_spot.iter_rows(named=True):
        # exchange_symbol = market["name"]
        base_i, quote_i = market["tokens"]

        base = df_tokens["name"][base_i]  # e.g. "PURR"
        quote = df_tokens["name"][quote_i]  # e.g. "USDC"
        tick = str(reverse_decimal_places(df_tokens["szDecimals"][base_i]))

        markets.append(
            MarketInfo(
                exchange=Common.HYPERLIQUID,
                exchange_symbol=str(market["name"]),
                product_symbol=f"{base}-{quote}-SPOT",
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
                price_precision=tick,
                size_precision=tick,
                min_size=tick,
            )
        )
    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)
