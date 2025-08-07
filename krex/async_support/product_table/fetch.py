import re
import polars as pl
from typing import Dict
from dataclasses import dataclass, asdict
from ...utils.decimal_utils import reverse_decimal_places
from ...utils.common import Common
from ...utils.common_dataframe import to_dataframe


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
    multiplier: str = "1"

    # contract
    size_per_contract: str = "1"

    def to_dict(self) -> Dict[str, str]:
        return asdict(self)


def clean_symbol_and_strip_number(symbol: str) -> str:
    symbol = re.sub(r"^\d+", "", symbol)
    symbol = re.sub(r"[$_]", "", symbol)
    return symbol


async def bybit() -> pl.DataFrame:
    from ..bybit._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    linear_data = []
    cursor = None
    while True:
        res_linear = await market_http.get_instruments_info(category="linear", cursor=cursor)
        linear_data.extend(res_linear["result"]["list"])
        if res_linear["result"]["nextPageCursor"] == "":
            break
        cursor = res_linear["result"]["nextPageCursor"]

    df_linear = to_dataframe(linear_data)

    for market in df_linear.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCoin"])
        quote = market["quoteCoin"]

        parts = market["symbol"].split("-")
        if len(parts) >= 2:
            expiry_str = parts[1]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"
        else:
            product_symbol = f"{base}-{quote}-SWAP"

        if market["contractType"] == "LinearFutures":
            product_type = "futures"
        else:
            product_type = "swap"

        markets.append(
            MarketInfo(
                exchange=Common.BYBIT,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type=product_type,
                exchange_type="linear",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["qtyStep"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
                min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
            )
        )

    res_inverse = await market_http.get_instruments_info(category="inverse")
    df_inverse = (
        to_dataframe(res_inverse["result"]["list"]) if "list" in res_inverse.get("result", {}) else pl.DataFrame()
    )
    for market in df_inverse.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCoin"])
        quote = market["quoteCoin"]

        parts = market["symbol"].split("-")
        if len(parts) >= 2:
            base, expiry_str = clean_symbol_and_strip_number(parts[0]), parts[1]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"
        else:
            product_symbol = f"{base}-{quote}-SWAP"

        if market["contractType"] == "LinearFutures":
            product_type = "futures"
        else:
            product_type = "swap"

        markets.append(
            MarketInfo(
                exchange=Common.BYBIT,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type=product_type,
                exchange_type="inverse",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["qtyStep"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
            )
        )

    res_spot = await market_http.get_instruments_info(category="spot")
    df_spot = to_dataframe(res_spot["result"]["list"]) if "list" in res_spot.get("result", {}) else pl.DataFrame()
    for market in df_spot.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCoin"])
        quote = market["quoteCoin"]
        product_symbol = f"{base}-{quote}-SPOT"

        markets.append(
            MarketInfo(
                exchange=Common.BYBIT,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
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
    await public_http.async_init()

    markets = []
    res_swap = await public_http.get_public_instruments(instType="SWAP")
    df_swap = to_dataframe(res_swap["data"]) if "data" in res_swap else pl.DataFrame()
    for market in df_swap.iter_rows(named=True):
        parts = market["instId"].split("-")
        if len(parts) >= 2:
            base, quote = clean_symbol_and_strip_number(parts[0]), parts[1]

        markets.append(
            MarketInfo(
                exchange=Common.OKX,
                exchange_symbol=market["instId"],
                product_symbol=clean_symbol_and_strip_number(market["instId"]),
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

    res_spot = await public_http.get_public_instruments(instType="SPOT")
    df_spot = to_dataframe(res_spot["data"]) if "data" in res_spot else pl.DataFrame()
    for market in df_spot.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCcy"])
        quote = market["quoteCcy"]

        markets.append(
            MarketInfo(
                exchange=Common.OKX,
                exchange_symbol=market["instId"],
                product_symbol=market["instId"] + "-SPOT",
                product_type="spot",
                exchange_type=market["instType"],
                base_currency=base,
                quote_currency=quote,
                price_precision=market["tickSz"],
                size_precision=market["lotSz"],
                min_size=market["minSz"],
            )
        )

    res_futures = await public_http.get_public_instruments(instType="FUTURES")
    df_futures = to_dataframe(res_futures["data"]) if "data" in res_futures else pl.DataFrame()
    for market in df_futures.iter_rows(named=True):
        parts = market["instId"].split("-")
        if len(parts) >= 2:
            base, quote = clean_symbol_and_strip_number(parts[0]), parts[1]

        markets.append(
            MarketInfo(
                exchange=Common.OKX,
                exchange_symbol=market["instId"],
                product_symbol=clean_symbol_and_strip_number(market["instId"]),
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
    await market_http.async_init()

    markets = []
    res_swap = await market_http.get_contracts_details()
    df_swap = to_dataframe(res_swap.get("data", {}).get("symbols", []))
    for market in df_swap.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["base_currency"])
        quote = market["quote_currency"]
        product_symbol = f"{base}-{quote}-SWAP"

        markets.append(
            MarketInfo(
                exchange=Common.BITMART,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="swap",
                exchange_type="swap",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["price_precision"],
                size_precision=market["vol_precision"],
                min_size=market["min_volume"],
                size_per_contract=market["contract_size"],
            )
        )

    res_spot = await market_http.get_trading_pairs_details()
    df_spot = to_dataframe(res_spot.get("data", {}).get("symbols", []))
    for market in df_spot.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["base_currency"])
        quote = market["quote_currency"]
        product_symbol = f"{base}-{quote}-SPOT"

        markets.append(
            MarketInfo(
                exchange=Common.BITMART,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
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
    await market_http.async_init()

    markets = []
    res_futures = await market_http.get_all_futures_contracts()
    df_futures = to_dataframe(res_futures)
    for market in df_futures.iter_rows(named=True):
        parts = market["name"].split("_")
        if len(parts) == 2:
            base, quote = clean_symbol_and_strip_number(parts[0]), parts[1]
            product_symbol = f"{base}-{quote}-SWAP"
        elif len(parts) == 3:
            base, quote, expiry_str = clean_symbol_and_strip_number(parts[0]), parts[1], parts[2]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"

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

    res_delivery = await market_http.get_all_delivery_contracts()
    df_deliver = to_dataframe(res_delivery)
    for market in df_deliver.iter_rows(named=True):
        parts = market["name"].split("_")
        if len(parts) == 2:
            base, quote = clean_symbol_and_strip_number(parts[0]), parts[1]
            product_symbol = f"{base}-{quote}-SWAP"
        elif len(parts) == 3:
            base, quote, expiry_str = clean_symbol_and_strip_number(parts[0]), parts[1], parts[2]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"

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

    res_spot = await market_http.get_spot_all_currency_pairs()
    df_spot = to_dataframe(res_spot)
    for market in df_spot.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["base"])
        quote = market["quote"]
        product_symbol = f"{base}-{quote}-SPOT"

        markets.append(
            MarketInfo(
                exchange=Common.GATEIO,
                exchange_symbol=market["id"],
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
                price_precision=reverse_decimal_places(market["precision"]),
                size_precision=reverse_decimal_places(market["amount_precision"]),
                min_size=market["min_base_amount"],
                min_notional=market["min_quote_amount"],
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def binance() -> pl.DataFrame:
    from ..binance._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    res_spot = await market_http.get_spot_exchange_info()
    df_spot = to_dataframe(res_spot.get("symbols", []))
    for market in df_spot.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseAsset"])
        quote = market["quoteAsset"]
        product_symbol = f"{base}-{quote}-SPOT"

        price_filter = next((f for f in market["filters"] if f["filterType"] == "PRICE_FILTER"), {})
        lot_size_filter = next((f for f in market["filters"] if f["filterType"] == "LOT_SIZE"), {})
        min_notional_filter = next((f for f in market["filters"] if f["filterType"] == "NOTIONAL"), {})

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
                min_notional=str(float(min_notional_filter.get("minNotional", "0"))),
            )
        )

    res_futures = await market_http.get_futures_exchange_info()
    df_futures = to_dataframe(res_futures.get("symbols", []))
    for market in df_futures.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseAsset"])
        quote = market["quoteAsset"]

        parts = market["symbol"].split("_")
        if len(parts) >= 2:
            expiry_str = parts[1]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"
        else:
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


async def hyperliquid() -> pl.DataFrame:
    from ..hyperliquid._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    res_prep = await market_http.meta()
    df_prep = to_dataframe(res_prep.get("universe", []))

    for idx, market in enumerate(df_prep.iter_rows(named=True)):
        coin = market["name"]
        tick = str(reverse_decimal_places(market["szDecimals"]))
        markets.append(
            MarketInfo(
                exchange=Common.HYPERLIQUID,
                exchange_symbol=f'["{coin}", {idx}]',
                product_symbol=f"{coin}-USD-SWAP",
                product_type="swap",
                exchange_type="perpetual",
                base_currency=coin,
                quote_currency="USD",
                price_precision=tick,
                size_precision=tick,
                min_size=tick,
            )
        )

    res_spot = await market_http.spot_meta()
    df_tokens = to_dataframe(res_spot.get("tokens", []))
    df_spot = to_dataframe(res_spot.get("universe", []))

    for idx, market in enumerate(df_spot.iter_rows(named=True)):
        # exchange_symbol = market["name"]
        base_i, quote_i = market["tokens"]

        base = df_tokens["name"][base_i]  # e.g. "PURR"
        quote = df_tokens["name"][quote_i]  # e.g. "USDC"
        tick = str(reverse_decimal_places(df_tokens["szDecimals"][base_i]))

        markets.append(
            MarketInfo(
                exchange=Common.HYPERLIQUID,
                exchange_symbol='["{}", {}]'.format(market["name"], 10000 + idx),
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


async def bingx() -> pl.DataFrame:
    from ..bingx._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    res = await market_http.get_swap_instrument_info()
    df = to_dataframe(res.get("data", []))

    for market in df.iter_rows(named=True):
        symbol = market["symbol"]

        if "-" in symbol:
            base, quote = clean_symbol_and_strip_number(symbol).rsplit("-", 1)

        product_symbol = f"{base}-{quote}-SWAP"

        price_precision_val = int(market.get("pricePrecision", 0))
        quantity_precision_val = int(market.get("quantityPrecision", 0))

        price_precision = str(reverse_decimal_places(price_precision_val)) if price_precision_val > 0 else "0"
        size_precision = str(reverse_decimal_places(quantity_precision_val)) if quantity_precision_val > 0 else "0"
        min_size = size_precision

        markets.append(
            MarketInfo(
                exchange=Common.BINGX,
                exchange_symbol=symbol,
                product_symbol=product_symbol,
                product_type="swap",
                exchange_type="perpetual",
                base_currency=base,
                quote_currency=quote,
                price_precision=price_precision,
                size_precision=size_precision,
                min_size=min_size,
                min_notional=str(market.get("tradeMinUSDT", "0")),
                size_per_contract=str(market.get("size", "1")),
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def kucoin() -> pl.DataFrame:
    from ..kucoin._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    res = await market_http.get_spot_instrument_info()
    df = to_dataframe(res.get("data", []))

    for market in df.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCurrency"])
        quote = market["quoteCurrency"]
        product_symbol = f"{base}-{quote}-SPOT"

        markets.append(
            MarketInfo(
                exchange=Common.KUCOIN,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["priceIncrement"],
                size_precision=market["baseIncrement"],
                min_size=market["baseMinSize"],
                min_notional=market["minFunds"] if market["minFunds"] else "0",
            )
        )

    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def ascendex() -> pl.DataFrame:
    from ..ascendex._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()
    markets = []
    res = await market_http.get_spot_instrument_info()
    data = res.get("data", [])
    for market in data:
        symbol = market.get("symbol", "")

        if "/" in symbol:
            base, quote = symbol.split("/")
        else:
            continue
        product_symbol = f"{clean_symbol_and_strip_number(base)}-{quote}-SPOT"
        markets.append(
            MarketInfo(
                exchange=Common.ASCENDEX,
                exchange_symbol=symbol,
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
                price_precision=str(market.get("tickSize", "0")),
                size_precision=str(market.get("lotSize", "0")),
                min_size=str(market.get("minQty", "0")),
                min_notional=str(market.get("minNotional", "0")),
            )
        )
    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)


async def bitmex() -> pl.DataFrame:
    from ..bitmex._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    res = await market_http.get_instrument_info(filter={"state": ["FFWCSX", "FFCCSX", "IFXXXP"]})

    if not isinstance(res, list):
        res = []

    typ_map = {
        "FFWCSX": "swap",
        "FFCCSX": "futures",
        "IFXXXP": "spot",
    }

    markets = []
    for market in res:
        typ = market.get("typ", "")
        product_type = typ_map.get(typ)
        if not product_type:
            continue

        symbol = market["symbol"]
        base = clean_symbol_and_strip_number(market["underlying"])
        quote = market["quoteCurrency"]
        price_precision = str(market["tickSize"])
        size_precision = str(market["lotSize"])
        min_size = str(market["lotSize"])
        size_per_contract = str(market["multiplier"])
        min_notional = "0"

        if typ == "IFXXXP":
            product_symbol = f"{base}-{quote}-SPOT"
        elif typ == "FFWCSX":
            product_symbol = f"{base}-{quote}-SWAP"
        elif typ == "FFCCSX":
            if (base + quote) in symbol:
                expiry_str = symbol.replace(base + quote, "", 1)
            else:
                expiry_str = symbol.replace(base, "", 1)
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"
        else:
            product_symbol = symbol

        markets.append(
            MarketInfo(
                exchange=Common.BITMEX,
                exchange_symbol=symbol,
                product_symbol=product_symbol,
                product_type=product_type,
                exchange_type=typ,
                base_currency=base,
                quote_currency=quote,
                price_precision=price_precision,
                size_precision=size_precision,
                min_size=min_size,
                min_notional=min_notional,
                size_per_contract=size_per_contract,
            ).to_dict()
        )

    return pl.DataFrame(markets)

async def zoomex() -> pl.DataFrame:
    from ..zoomex._market_http import MarketHTTP

    market_http = MarketHTTP()
    await market_http.async_init()

    markets = []
    linear_data = []
    cursor = None
    while True:
        res_linear = await market_http.get_instruments_info(category="linear", cursor=cursor)
        linear_data.extend(res_linear["result"]["list"])
        if res_linear["result"]["nextPageCursor"] == "":
            break
        cursor = res_linear["result"]["nextPageCursor"]

    df_linear = to_dataframe(linear_data)
    
    for market in df_linear.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCoin"])
        quote = market["quoteCoin"]

        parts = market["symbol"].split("-")
        if len(parts) >= 2:
            expiry_str = parts[1]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"
        else:
            product_symbol = f"{base}-{quote}-SWAP"

        if market["contractType"] == "LinearFutures":
            product_type = "futures"
        else:
            product_type = "swap"

        markets.append(
            MarketInfo(
                exchange=Common.ZOOMEX,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type=product_type,
                exchange_type="linear",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["qtyStep"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
                min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
            )
        )

    res_inverse = await market_http.get_instruments_info(category="inverse")
    df_inverse = (
        to_dataframe(res_inverse["result"]["list"]) if "list" in res_inverse.get("result", {}) else pl.DataFrame()
    )
    for market in df_inverse.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCoin"])
        quote = market["quoteCoin"]

        parts = market["symbol"].split("-")
        if len(parts) >= 2:
            base, expiry_str = clean_symbol_and_strip_number(parts[0]), parts[1]
            product_symbol = f"{base}-{quote}-{expiry_str}-SWAP"
        else:
            product_symbol = f"{base}-{quote}-SWAP"

        if market["contractType"] == "LinearFutures":
            product_type = "futures"
        else:
            product_type = "swap"

        markets.append(
            MarketInfo(
                exchange=Common.ZOOMEX,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type=product_type,
                exchange_type="inverse",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["qtyStep"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
            )
        )

    res_spot = await market_http.get_instruments_info(category="spot")
    df_spot = to_dataframe(res_spot["result"]["list"]) if "list" in res_spot.get("result", {}) else pl.DataFrame()
    for market in df_spot.iter_rows(named=True):
        base = clean_symbol_and_strip_number(market["baseCoin"])
        quote = market["quoteCoin"]
        product_symbol = f"{base}-{quote}-SPOT"

        markets.append(
            MarketInfo(
                exchange=Common.ZOOMEX,
                exchange_symbol=market["symbol"],
                product_symbol=product_symbol,
                product_type="spot",
                exchange_type="spot",
                base_currency=base,
                quote_currency=quote,
                price_precision=market["priceFilter"]["tickSize"],
                size_precision=market["lotSizeFilter"]["basePrecision"],
                min_size=market["lotSizeFilter"]["minOrderQty"],
                min_notional=market["lotSizeFilter"].get("minNotionalValue", "0"),
            )
        )
    markets = [market.to_dict() for market in markets]
    return pl.DataFrame(markets)
