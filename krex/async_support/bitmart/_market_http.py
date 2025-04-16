import pandas as pd
from ._http_manager import HTTPManager
from .endpoints.market import SpotMarket, FuturesMarket
from ...utils.common import Common
from ...utils.timeframe_utils import bitmart_convert_timeframe


class MarketHTTP(HTTPManager):
    async def get_spot_currencies(self) -> pd.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_SPOT_CURRENCIES,
            query=None,
        )
        return pd.DataFrame(res.get("data", {}).get("currencies", []))

    async def get_trading_pairs(self) -> pd.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS,
            query=None,
        )
        return pd.DataFrame(res["data"]) if "data" in res else pd.DataFrame()

    async def get_trading_pairs_details(self) -> pd.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TRADING_PAIRS_DETAILS,
            query=None,
        )

        if "data" not in res or "symbols" not in res["data"]:
            return pd.DataFrame()
        return pd.DataFrame(res["data"]["symbols"])

    async def get_ticker_of_all_pairs(self) -> pd.DataFrame:
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_TICKER_OF_ALL_PAIRS,
            query=None,
        )
        return pd.DataFrame(res["data"]) if "data" in res else pd.DataFrame()

    async def get_ticker_of_a_pair(
        self,
        product_symbol: str,
    ) -> pd.DataFrame:
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
        return pd.DataFrame([res["data"]]) if "data" in res else pd.DataFrame()

    async def get_spot_kline(
        self,
        product_symbol: str,
        interval: str,
        before: int = None,
        after: int = None,
        limit: int = None,
    ) -> pd.DataFrame:
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
        if "data" not in res or not res["data"]:
            return pd.DataFrame()

        df = pd.DataFrame(res["data"])
        df.columns = ["datetime", "open", "high", "low", "close", "volume", "quote_volume"]
        df["datetime"] = pd.to_datetime(df["datetime"].astype(int), unit="s")
        df.set_index("datetime", inplace=True)
        return df

    async def get_contracts_details(
        self,
        product_symbol: str = None,
    ) -> pd.DataFrame:
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

        if "data" not in res or "symbols" not in res["data"]:
            return pd.DataFrame()
        return pd.DataFrame(res["data"]["symbols"])

    async def get_depth(
        self,
        product_symbol: str,
    ) -> pd.DataFrame:
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
        if "data" not in res:
            return pd.DataFrame()

        data = res["data"]
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

        return pd.DataFrame(rows)

    async def get_contract_kline(
        self,
        product_symbol: str,
        interval: str,
        start_time: int,
        end_time: int,
    ) -> pd.DataFrame:
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
        df = pd.DataFrame(data["data"])
        columns_map = {
            "timestamp": "datetime",
            "open_price": "open",
            "high_price": "high",
            "low_price": "low",
            "close_price": "close",
            "volume": "volume",
        }
        df.rename(columns=columns_map, inplace=True)
        df["datetime"] = pd.to_datetime(df["datetime"], unit="s")
        df.set_index("datetime", inplace=True)
        return df

    async def get_current_funding_rate(
        self,
        product_symbol: str,
    ) -> pd.DataFrame:
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
        return pd.DataFrame([res["data"]]) if "data" in res else pd.DataFrame()

    async def get_funding_rate_history(
        self,
        product_symbol: str,
        limit: int = None,
    ) -> pd.DataFrame:
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
        return pd.DataFrame(res["data"]) if "data" in res else pd.DataFrame()
