from ._http_manager import HTTPManager
from .endpoints.trade import Trade
from ..utils.common import Common


class TradeHTTP(HTTPManager):
    def place_order(
        self,
        product_symbol: str,
        tdMode: str,
        side: str,
        ordType: str,
        sz: str,
        ccy: str = None,
        clOrdId: str = None,
        tag: str = None,
        posSide: str = None,
        px: str = None,
        pxUsd: str = None,
        pxVol: str = None,
        reduceOnly: bool = False,
        tgtCcy: str = None,
        banAmend: bool = False,
        quickMgnType: str = None,
        stpId: str = None,
        stpMode: str = None,
    ):
        """
        :param product_symbol: str
        :param tdMode: str
        :param side: str
        :param ordType: str
        :param sz: str
        :param ccy: str
        :param clOrdId: str
        :param tag: str
        :param posSide: str
        :param px: str
        :param pxUsd: str
        :param pxVol: str
        :param reduceOnly: bool
        :param tgtCcy: str
        :param banAmend: bool
        :param quickMgnType: str
        :param stpId: str
        :param stpMode: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
            "tdMode": tdMode,
            "side": side,
            "ordType": ordType,
            "sz": sz,
        }
        if ccy is not None:
            payload["ccy"] = ccy
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId
        if tag is not None:
            payload["tag"] = tag
        if posSide is not None:
            payload["posSide"] = posSide
        if px is not None:
            payload["px"] = px
        if pxUsd is not None:
            payload["pxUsd"] = pxUsd
        if pxVol is not None:
            payload["pxVol"] = pxVol
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if tgtCcy is not None:
            payload["tgtCcy"] = tgtCcy
        if banAmend is not None:
            payload["banAmend"] = banAmend
        if quickMgnType is not None:
            payload["quickMgnType"] = quickMgnType
        if stpId is not None:
            payload["stpId"] = stpId
        if stpMode is not None:
            payload["stpMode"] = stpMode

        return self._request(
            method="POST",
            path=Trade.PLACE_ORDER,
            query=payload,
        )

    def place_market_order(
        self,
        product_symbol: str,
        tdMode: str,
        side: str,
        sz: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side=side,
            ordType="market",
            sz=sz,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_market_buy_order(
        self,
        product_symbol: str,
        tdMode: str,  # cash or cross
        sz: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_market_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side="buy",
            sz=sz,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_market_sell_order(
        self,
        product_symbol: str,
        tdMode: str,
        sz: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_market_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side="sell",
            sz=sz,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_limit_order(
        self,
        product_symbol: str,
        tdMode: str,
        side: str,
        sz: str,
        px: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side=side,
            ordType="limit",
            sz=sz,
            px=px,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_limit_buy_order(
        self,
        product_symbol: str,
        tdMode: str,
        sz: str,
        px: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_limit_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side="buy",
            sz=sz,
            px=px,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_limit_sell_order(
        self,
        product_symbol: str,
        tdMode: str,
        sz: str,
        px: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_limit_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side="sell",
            sz=sz,
            px=px,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_post_only_limit_order(
        self,
        product_symbol: str,
        tdMode: str,
        side: str,
        sz: str,
        px: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side=side,
            ordType="post_only",
            sz=sz,
            px=px,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_post_only_limit_buy_order(
        self,
        product_symbol: str,
        tdMode: str,
        sz: str,
        px: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_post_only_limit_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side="buy",
            sz=sz,
            px=px,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def place_post_only_limit_sell_order(
        self,
        product_symbol: str,
        tdMode: str,
        sz: str,
        px: str,
        reduceOnly: bool = None,
        ccy: str = None,
    ):
        return self.place_post_only_limit_order(
            product_symbol=product_symbol,
            tdMode=tdMode,
            side="sell",
            sz=sz,
            px=px,
            reduceOnly=reduceOnly,
            ccy=ccy,
        )

    def cancel_order(
        self,
        product_symbol: str,
        ordId: str = None,
        clOrdId: str = None,
    ):
        """
        :param product_symbol: str
        :param ordId: str
        :param clOrdId: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if ordId is not None:
            payload["ordId"] = ordId
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId

        return self._request(
            method="POST",
            path=Trade.CANCEL_ORDER,
            query=payload,
        )

    def cancel_all_orders(
        self,
        product_symbol: str = None,
    ):
        """
        :param product_symbol: str
        :param ordId: str
        :param clOrdId: str
        """
        payload = []

        all_orders = self.get_order_list()
        all_orders = all_orders["data"]
        if product_symbol is not None:
            exchange_symbol = self.ptm.get_exchange_symbol(product_symbol, Common.OKX)
            for order in all_orders:
                if order["instId"] == exchange_symbol:
                    payload.append(
                        {
                            "instId": order["instId"],
                            "ordId": order["ordId"],
                            "clOrdId": order["clOrdId"],
                        }
                    )
        else:
            for order in all_orders:
                payload.append(
                    {
                        "instId": order["instId"],
                        "ordId": order["ordId"],
                        "clOrdId": order["clOrdId"],
                    }
                )

        return self._request(
            method="POST",
            path=Trade.CANCEL_BATCH_ORDERS,
            query=payload,
        )

    def amend_order(
        self,
        product_symbol: str,
        ordId: str = None,
        clOrdId: str = None,
        newSz: str = None,
        newPx: str = None,
        newPxUsd: str = None,
        newPxVol: str = None,
        cxlOnFail: str = None,
        reqId: str = None,
    ):
        """
        :param product_symbol: str
        :param ordId: str
        :param clOrdId: str
        :param newSz: str
        :param newPx: str
        :param newPxUsd: str
        :param newPxVol: str
        :param cxlOnFail: str
        :param reqId: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if ordId is not None:
            payload["ordId"] = ordId
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId
        if newSz is not None:
            payload["newSz"] = newSz
        if newPx is not None:
            payload["newPx"] = newPx
        if newPxUsd is not None:
            payload["newPxUsd"] = newPxUsd
        if newPxVol is not None:
            payload["newPxVol"] = newPxVol
        if cxlOnFail is not None:
            payload["cxlOnFail"] = cxlOnFail
        if reqId is not None:
            payload["reqId"] = reqId

        return self._request(
            method="POST",
            path=Trade.AMEND_ORDER,
            query=payload,
        )

    def amend_multiple_orders(
        self,
        product_symbol: str,
        ordId: str = None,
        clOrdId: str = None,
        newSz: str = None,
        newPx: str = None,
        newPxUsd: str = None,
        newPxVol: str = None,
        cxlOnFail: str = None,
        reqId: str = None,
    ):
        """
        :param product_symbol: str
        :param ordId: str
        :param clOrdId: str
        :param newSz: str
        :param newPx: str
        :param newPxUsd: str
        :param newPxVol: str
        :param cxlOnFail: str
        :param reqId: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if ordId is not None:
            payload["ordId"] = ordId
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId
        if newSz is not None:
            payload["newSz"] = newSz
        if newPx is not None:
            payload["newPx"] = newPx
        if newPxUsd is not None:
            payload["newPxUsd"] = newPxUsd
        if newPxVol is not None:
            payload["newPxVol"] = newPxVol
        if cxlOnFail is not None:
            payload["cxlOnFail"] = cxlOnFail
        if reqId is not None:
            payload["reqId"] = reqId

        return self._request(
            method="POST",
            path=Trade.AMEND_BATCH_ORDER,
            query=payload,
        )

    def close_positions(
        self,
        product_symbol: str,
        mgnMode: str,
        posSide: str = None,
        autoCxl: bool = None,
        ccy: str = None,
    ):
        """
        :param product_symbol: str
        :param mgnMode: str
        :param posSide: str
        :param ccy: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(product_symbol, Common.OKX),
            "mgnMode": mgnMode,
        }
        if posSide is not None:
            payload["posSide"] = posSide
        if autoCxl is not None:
            payload["autoCxl"] = autoCxl
        if ccy is not None:
            payload["ccy"] = ccy

        return self._request(
            method="POST",
            path=Trade.CLOSE_POSITION,
            query=payload,
        )

    def get_order(
        self,
        product_symbol: str,
        ordId: str = None,
        clOrdId: str = None,
    ):
        """
        :param product_symbol: str
        :param ordId: str
        :param clOrdId: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
        }
        if ordId is not None:
            payload["ordId"] = ordId
        if clOrdId is not None:
            payload["clOrdId"] = clOrdId

        res = self._request(
            method="GET",
            path=Trade.ORDER_INFO,
            query=payload,
        )
        return res

    def get_order_list(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordType: str = None,
        state: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        :param product_symbol: str
        :param ordType: str
        :param state: str
        :param limit: str
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordType is not None:
            payload["ordType"] = ordType
        if state is not None:
            payload["state"] = state
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Trade.ORDERS_PENDING,
            query=payload,
        )
        return res

    def get_orders_history(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordType: str = None,
        state: str = None,
        category: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        :param product_symbol: str
        :param ordType: str
        :param state: str
        :param category: str
        :param begin: str
        :param end: str
        :param limit: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordType is not None:
            payload["ordType"] = ordType
        if state is not None:
            payload["state"] = state
        if category is not None:
            payload["category"] = category
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Trade.ORDERS_HISTORY,
            query=payload,
        )
        return res

    def get_orders_history_archive(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordType: str = None,
        state: str = None,
        category: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        :param product_symbol: str
        :param ordType: str
        :param state: str
        :param category: str
        :param begin: str
        :param end: str
        :param limit: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordType is not None:
            payload["ordType"] = ordType
        if state is not None:
            payload["state"] = state
        if category is not None:
            payload["category"] = category
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Trade.ORDERS_HISTORY_ARCHIVE,
            query=payload,
        )
        return res

    def get_fills(
        self,
        instType: str = None,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordId: str = None,
        subType: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        :param product_symbol: str
        :param ordId: str
        :param subType: str
        :param begin: str
        :param end: str
        :param limit: str
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordId is not None:
            payload["ordId"] = ordId
        if subType is not None:
            payload["subType"] = subType
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Trade.ORDER_FILLS,
            query=payload,
        )
        return res

    def get_fills_history(
        self,
        instType: str,
        uly: str = None,
        instFamily: str = None,
        product_symbol: str = None,
        ordId: str = None,
        subType: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param uly: str
        :param instFamily: str
        :param product_symbol: str
        :param ordId: str
        :param subType: str
        :param begin: str
        :param end: str
        :param limit: str
        """
        payload = {
            "instType": instType,
        }
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ordId is not None:
            payload["ordId"] = ordId
        if subType is not None:
            payload["subType"] = subType
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Trade.ORDERS_FILLS_HISTORY,
            query=payload,
        )
        return res

    def get_account_rate_limit(self):
        res = self._request(
            method="GET",
            path=Trade.ACCOUNT_RATE_LIMIT,
            query=None,
        )
        return res
