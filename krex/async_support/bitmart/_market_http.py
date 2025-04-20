import polars as pl
from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket, FuturesMarket
from ...utils.common import Common
from ...utils.timeframe_utils import bitmart_convert_timeframe


class MarketHTTP(HTTPManager):
    def _to_dataframe(self, data, schema: list[str] = None) -> pl.DataFrame:
        if not data:
            return pl.DataFrame()

        if isinstance(data, list):
            if schema:
                return pl.DataFrame(data, schema=schema, orient="row")
            elif all(isinstance(item, dict) for item in data):
                return pl.DataFrame(data)
            else:
                return pl.DataFrame(data, orient="row")

        if isinstance(data, dict):
            return pl.DataFrame([data])

        return pl.DataFrame()

    async def get_spot_currencies(self) -> pl.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_CURRENCIES,
            query=None,
        )
        return self._to_dataframe(res.get("data", {}).get("currencies", []))

    async def get_trading_pairs(self) -> pl.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS,
            query=None,
        )
        return self._to_dataframe(res.get("data", []))

    async def get_trading_pairs_details(self) -> pl.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS_DETAILS,
            query=None,
        )
        return self._to_dataframe(res.get("data", {}).get("symbols", []))

    async def get_ticker_of_all_pairs(self) -> pl.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_ALL_PAIRS,
            query=None,
        )
        schema = [
            "symbol",
            "last_price",
            "volume",
            "quote_volume",
            "open_price",
            "high_price",
            "low_price",
            "price_change_percent",
            "bid_price",
            "bid_size",
            "ask_price",
            "ask_size",
            "timestamp",
        ]
        return self._to_dataframe(res.get("data", []), schema=schema)

    async def get_ticker_of_a_pair(
        self,
        product_symbol: str,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
        }

        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_A_PAIR,
            query=payload,
        )
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    async def get_spot_kline(
        self,
        product_symbol: str,
        interval: str,
        before: int = None,
        after: int = None,
        limit: int = None,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        :param before: int
        :param after: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
        }
        if interval is not None:
            payload["step"] = bitmart_convert_timeframe(interval)
        if before is not None:
            payload["before"] = before
        if after is not None:
            payload["after"] = after
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_KLINE,
            query=payload,
        )
        data = res.get("data", [])
        if not data:
            return pl.DataFrame()

        df = pl.DataFrame(
            data, schema=["timestamp", "open", "high", "low", "close", "volume", "quote_volume"], orient="row"
        )
        return df

    async def get_contracts_details(
        self,
        product_symbol: str = None,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        """
        payload = {}
        if product_symbol is not None:
            payload["symbol"] = self.ptm.get_exchange_symbol(product_symbol, Common.BITMART)

        res = await self._request(
            method="GET",
            path=FuturesMarket.GET_CONTRACTS_DETAILS,
            query=payload,
        )
        return self._to_dataframe(res.get("data", {}).get("symbols", []))

    async def get_depth(
        self,
        product_symbol: str,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
        }

        res = await self._request(
            method="GET",
            path=FuturesMarket.GET_DEPTH,
            query=payload,
        )
        data = res.get("data", {})
        rows = []

        cum = 0
        for ask in data.get("asks", []):
            price, amount, _ = ask
            cum += float(amount)
            rows.append(
                {
                    "side": "ask",
                    "price": float(price),
                    "amount": float(amount),
                    "cum_amount": cum,
                }
            )

        cum = 0
        for bid in data.get("bids", []):
            price, amount, _ = bid
            cum += float(amount)
            rows.append(
                {
                    "side": "bid",
                    "price": float(price),
                    "amount": float(amount),
                    "cum_amount": cum,
                }
            )

        return self._to_dataframe(rows)

    async def get_contract_kline(
        self,
        product_symbol: str,
        interval: str,
        start_time: int,
        end_time: int,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        :param startTime: int
        :param endTime: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
            "step": bitmart_convert_timeframe(interval),
            "start_time": start_time,
            "end_time": end_time,
        }

        data = await self._request(
            method="GET",
            path=FuturesMarket.GET_CONTRACTS_KLINE,
            query=payload,
        )
        raw = data.get("data", [])
        if not raw:
            return pl.DataFrame()
        df = self._to_dataframe(raw).rename(
            {
                "timestamp": "timestamp",
                "open_price": "open",
                "high_price": "high",
                "low_price": "low",
                "close_price": "close",
                "volume": "volume",
            }
        )
        return df

    async def get_current_funding_rate(
        self,
        product_symbol: str,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
        }

        res = await self._request(
            method="GET",
            path=FuturesMarket.GET_CURRENT_FUNDING_RATE,
            query=payload,
        )
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()

    async def get_funding_rate_history(
        self,
        product_symbol: str,
        limit: int = None,
    ) -> pl.DataFrame:
        """
        :param product_symbol: str
        :param limit: int
        """
        payload = {
            "symbol": self.ptm.get_exchange_symbol(product_symbol, Common.BITMART),
        }
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=FuturesMarket.GET_FUNDING_RATE_HISTORY,
            query=payload,
        )
        return self._to_dataframe(res["data"]) if "data" in res else pl.DataFrame()
