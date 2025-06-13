from ._http_manager import HTTPManager
from .endpoints.market import DeliveryMarket, FutureMarket, SpotMarket
from ...utils.common import Common


class MarketHTTP(HTTPManager):
    async def get_all_futures_contracts(
        self,
        ccy: str = "usdt",  # or "btc"
        limit: int = None,
        offset: int = None,
    ):
        """
        :param ccy: str
        :param limit: int
        :param offset: int
        """
        path_params = {
            "settle": ccy,
        }

        payload = {}
        if limit:
            payload["limit"] = limit
        if offset:
            payload["offset"] = offset

        res = await self._request(
            method="GET",
            path=FutureMarket.GET_ALL_CONTRACTS,
            path_params=path_params,
            query=payload,
            signed=False,
        )
        return res

    async def get_a_single_futures_contract(
        self,
        product_symbol: str,
        ccy: str = "usdt",  # or "btc"
    ):
        """
        :param product_symbol: str
        :param ccy: str
        """
        path_params = {
            "settle": ccy,
            "contract": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }

        res = await self._request(
            method="GET",
            path=FutureMarket.GET_A_SINGLE_CONTRACT,
            path_params=path_params,
            signed=False,
        )
        return res

    async def get_contract_order_book(
        self,
        product_symbol: str,
        ccy: str = "usdt",  # or "btc"
        path: str = "futures",
        interval: str = None,
        limit: int = None,
        with_id: bool = False,
    ):
        """
        :param product_symbol: int
        :param ccy: str
        :param path: str
        :param interval: int
        :param limit: int
        :param with_id: bool
        """
        path_params = {
            "settle": ccy,
        }

        payload = {
            "contract": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }
        if interval:
            payload["interval"] = interval
        if limit:
            payload["limit"] = limit
        if with_id:
            payload["with_id"] = with_id

        if path == "futures":
            path_ = FutureMarket.ORDER_BOOK
        elif path == "delivery":
            path_ = DeliveryMarket.ORDER_BOOK
        else:
            raise ValueError(f"Unsupported path: {path}")

        res = await self._request(
            method="GET",
            path=path_,
            path_params=path_params,
            query=payload,
            signed=False,
        )
        return res

    async def get_contract_kline(
        self,
        product_symbol: str,
        ccy: str = "usdt",  # or "btc"
        path: str = "futures",
        from_timestamp: int = None,
        to_timestamp: int = None,
        limit: int = None,
        interval: str = None,
    ):
        """
        :param product_symbol: int
        :param ccy: str
        :param path: str
        :param from_timestamp : int
        :param to_timestamp : int
        :param limit: bool
        :param interval: str
        """
        path_params = {
            "settle": ccy,
        }

        payload = {
            "contract": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }
        if from_timestamp:
            payload["from"] = from_timestamp
        if to_timestamp:
            payload["to"] = to_timestamp
        if limit:
            payload["limit"] = limit
        if interval:
            payload["interval"] = interval

        if path == "futures":
            path_ = FutureMarket.GET_KLINE
        elif path == "delivery":
            path_ = DeliveryMarket.GET_KLINE
        else:
            raise ValueError(f"Unsupported path: {path}")

        res = await self._request(
            method="GET",
            path=path_,
            path_params=path_params,
            query=payload,
            signed=False,
        )
        return res

    async def get_contract_list_tickers(
        self,
        product_symbol: str,
        ccy: str = "usdt",  # or "btc"
        path: str = "futures",
    ):
        """
        :param product_symbol: int
        :param ccy: str
        :param path: str
        """
        path_params = {
            "settle": ccy,
        }

        payload = {
            "contract": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }

        if path == "futures":
            path_ = FutureMarket.LIST_TICKERS
        elif path == "delivery":
            path_ = DeliveryMarket.LIST_TICKERS
        else:
            raise ValueError(f"Unsupported path: {path}")

        res = await self._request(
            method="GET",
            path=path_,
            path_params=path_params,
            query=payload,
            signed=False,
        )
        return res

    async def get_futures_funding_rate_history(
        self,
        product_symbol: str,
        ccy: str = "usdt",  # or "btc"
        limit: int = None,
        from_timestamp: int = None,
        to_timestamp: int = None,
    ):
        """
        :param product_symbol: int
        :param ccy: str
        :param limit: int
        :param from_timestamp: int
        :param to_timestamp: int
        """
        path_params = {
            "settle": ccy,
        }

        payload = {
            "contract": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }
        if limit:
            payload["limit"] = limit
        if from_timestamp:
            payload["from"] = from_timestamp
        if to_timestamp:
            payload["to"] = to_timestamp

        res = await self._request(
            method="GET",
            path=FutureMarket.FUNDING_RATE_HISTORY,
            path_params=path_params,
            query=payload,
            signed=False,
        )
        return res

    async def get_all_delivery_contracts(self):
        path_params = {
            "settle": "usdt",
        }

        res = await self._request(
            method="GET",
            path=DeliveryMarket.GET_ALL_CONTRACTS,
            path_params=path_params,
            signed=False,
        )
        return res

    async def get_spot_all_currency_pairs(self):
        res = await self._request(
            method="GET",
            path=SpotMarket.GET_ALL_CURRENCY_PAIRS,
            signed=False,
        )
        return res

    async def get_spot_order_book(
        self,
        product_symbol: str,
        interval: str = None,
        limit: int = None,
        with_id: bool = False,
    ):
        """
        :param product_symbol: int
        :param interval: int
        :param limit: int
        :param with_id: bool
        """
        payload = {
            "currency_pair": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }
        if interval:
            payload["interval"] = interval
        if limit:
            payload["limit"] = limit
        if with_id:
            payload["with_id"] = with_id

        res = await self._request(
            method="GET",
            path=SpotMarket.ORDER_BOOK,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_kline(
        self,
        product_symbol: str,
        from_timestamp: int = None,
        to_timestamp: int = None,
        limit: int = None,
        interval: str = None,
    ):
        """
        :param product_symbol: int
        :param from_timestamp : int
        :param to_timestamp : int
        :param limit: bool
        :param interval: str
        """
        payload = {
            "currency_pair": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }
        if from_timestamp:
            payload["from"] = from_timestamp
        if to_timestamp:
            payload["to"] = to_timestamp
        if limit:
            payload["limit"] = limit
        if interval:
            payload["interval"] = interval

        res = await self._request(
            method="GET",
            path=SpotMarket.GET_KLINE,
            query=payload,
            signed=False,
        )
        return res

    async def get_spot_list_tickers(
        self,
        product_symbol: str,
        timezone: str = None,
    ):
        """
        :param product_symbol: int
        :param timezone: str
        """

        payload = {
            "currency_pair": self.ptm.get_exchange_symbol(Common.GATEIO, product_symbol),
        }
        if timezone:
            payload["timezone"] = timezone

        res = await self._request(
            method="GET",
            path=SpotMarket.LIST_TICKERS,
            query=payload,
            signed=False,
        )
        return res
