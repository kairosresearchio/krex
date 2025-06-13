from ._http_manager import HTTPManager
from ._market_http import MarketHTTP
from .endpoint.path import Path
from .endpoint.trade import Trade
from ...utils.common import Common
import json


class TradeHTTP(HTTPManager):
    async def place_order(
        self,
        product_symbol: str,
        isBuy: bool,
        price: str,
        size: str,
        reduceOnly: bool,
        tif: str = None,
        isMarket: bool = None,
        triggerPx: str = None,
        tpsl: str = None,
        cloid: str = None,
        grouping: str = "na",
        builder_address: str = None,
        fee_ten_bp: int = None,
        vaultAddress: str = None,
        expireAfter: int = None,
    ):
        """
        :param product_symbol: str
        :param isBuy: bool
        :param price: str
        :param size: str
        :param reduceOnly: bool
        :param tif: str
        :param isMarket: bool
        :param triggerPx: str
        :param tpsl: str
        :param cloid: str
        :param grouping: str
        :param builder_address: str
        :param fee_ten_bp: int
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.ORDER,
            "orders": [
                {
                    "a": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
                    "b": isBuy,
                    "p": price,
                    "s": size,
                    "r": reduceOnly,
                }
            ],
            "grouping": grouping,
        }

        if tif is not None or isMarket:
            t = {}
            if tif is not None:
                t["limit"] = {"tif": tif}
            else:
                t["trigger"] = {
                    "isMarket": isMarket,
                    "triggerPx": triggerPx,
                    "tpsl": tpsl,
                }
            action["orders"][0]["t"] = t

        if cloid is not None:
            action["orders"][0]["c"] = cloid
        if builder_address is not None:
            action["builder"]["b"] = builder_address
        if fee_ten_bp is not None:
            action["feeTenBp"] = fee_ten_bp

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }

        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def place_future_market_order(
        self,
        product_symbol: str,
        isBuy: bool,
        size: str,
        triggerPx: str = None,
        tpsl: str = None,
    ):
        market_http = MarketHTTP()
        await market_http.async_init()
        result = await market_http.meta_and_asset_ctxs()
        exchange_symbol = int(self.ptm.get_exchange_symbol(product_symbol, Common.HYPERLIQUID))
        price = result[1][exchange_symbol]["midPx"]

        return await self.place_order(
            product_symbol=product_symbol,
            isBuy=isBuy,
            price=price.split(".", 1)[0],
            size=size,
            reduceOnly=False,
            isMarket=True,
            triggerPx=triggerPx,
            tpsl=tpsl,
        )

    async def place_future_market_buy_order(
        self,
        product_symbol: str,
        size: str,
        triggerPx: str = None,
        tpsl: str = None,
    ):
        return await self.place_future_market_order(
            product_symbol=product_symbol,
            isBuy=True,
            size=size,
            triggerPx=triggerPx,
            tpsl=tpsl,
        )

    async def place_future_market_sell_order(
        self,
        product_symbol: str,
        size: str,
        triggerPx: str = None,
        tpsl: str = None,
    ):
        return await self.place_future_market_order(
            product_symbol=product_symbol,
            isBuy=False,
            size=size,
            triggerPx=triggerPx,
            tpsl=tpsl,
        )

    async def place_future_limit_order(
        self,
        product_symbol: str,
        isBuy: bool,
        price,
        size: str,
        tif: str,
    ):
        return await self.place_order(
            product_symbol=product_symbol, isBuy=isBuy, price=price, size=size, reduceOnly=False, tif=tif
        )

    async def place_future_limit_buy_order(
        self,
        product_symbol: str,
        price,
        size: str,
        tif: str,
    ):
        return await self.place_order(
            product_symbol=product_symbol, isBuy=True, price=price, size=size, reduceOnly=False, tif=tif
        )

    async def place_future_limit_sell_order(
        self,
        product_symbol: str,
        price,
        size: str,
        tif: str,
    ):
        return await self.place_order(
            product_symbol=product_symbol, isBuy=False, price=price, size=size, reduceOnly=False, tif=tif
        )

    async def cancel_order(self, product_symbol: str, oid: int, vaultAddress: str = None, expireAfter: int = None):
        """
        :param product_symbol: str
        :param oid: str
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.CANCEL,
            "cancels": [
                {
                    "a": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
                    "o": oid,
                }
            ],
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }
        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def cancel_order_by_cloid(
        self, product_symbol: str, cloid: str, vaultAddress: str = None, expireAfter: int = None
    ):
        """
        :param product_symbol: str
        :param cloid: str
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.CANCELBYCLOID,
            "cancels": [
                {
                    "asset": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
                    "cloid": cloid,
                }
            ],
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }
        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def schedule_cancel(self, time: int = None, vaultAddress: str = None, expireAfter: int = None):
        """
        :param time: int
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.SCHEDULECANCEL,
            "time": time,
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }
        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def modify_order(
        self,
        oid: int,
        product_symbol: str,
        isBuy: bool,
        price: str,
        size: str,
        reduceOnly: bool,
        tif: str = None,
        isMarket: bool = None,
        triggerPx: str = None,
        tpsl: str = None,
        cloid: str = None,
        vaultAddress: str = None,
        expireAfter: int = None,
    ):
        """
        :param oid: int
        :param product_symbol: str
        :param isBuy: bool
        :param price: str
        :param size: str
        :param reduceOnly: bool
        :param tif: str
        :param isMarket: bool
        :param triggerPx: str
        :param tpsl: str
        :param cloid: str
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.MODIFY,
            "oid": oid,
            "order": {
                "a": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
                "b": isBuy,
                "p": price,
                "s": size,
                "r": reduceOnly,
            },
        }

        if tif is not None or isMarket:
            t = {}
            if tif is not None:
                t["limit"] = {"tif": tif}
            else:
                t["trigger"] = {
                    "isMarket": isMarket,
                    "triggerPx": triggerPx,
                    "tpsl": tpsl,
                }
            action["order"]["t"] = t
        if cloid is not None:
            action["order"]["c"] = cloid

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }

        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def modify_batch_orders(self, modifies: list, vaultAddress: str = None, expireAfter: int = None):
        """
        :param modifies: list
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {"type": Trade.BATCHMODIFY, "modifies": modifies}

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }

        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def update_leverage(
        self, product_symbol: str, isCross: bool, leverage: int, vaultAddress: str = None, expireAfter: int = None
    ):
        """
        :param product_symbol: str
        :param isCross: bool
        :param leverage: int
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.UPDATELEVERAGE,
            "asset": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
            "isCross": isCross,
            "leverage": leverage,
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }
        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def update_isolate_margin(
        self, product_symbol: str, isBuy: bool, ntli: int, vaultAddress: str = None, expireAfter: int = None
    ):
        """
        :param product_symbol: str
        :param isBuy: bool
        :param ntli: int
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.UPDATEISOLATEMARGIN,
            "asset": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
            "isBuy": isBuy,
            "ntli": ntli,
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }
        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def place_twap_order(
        self,
        product_symbol: str,
        isBuy: bool,
        size: str,
        reduceOnly: bool,
        minutes: int,
        randomize: bool,
        vaultAddress: str = None,
        expireAfter: int = None,
    ):
        """
        :param product_symbol: str
        :param isBuy: bool
        :param size: str
        :param reduceOnly: bool
        :param minutes: int
        :param randomize: bool
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.TWAPORDER,
            "twap": {
                "a": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
                "b": isBuy,
                "s": size,
                "r": reduceOnly,
                "m": minutes,
                "t": randomize,
            },
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }

        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res

    async def cancel_twap_order(
        self, product_symbol: str, twap_id: int, vaultAddress: str = None, expireAfter: int = None
    ):
        """
        :param product_symbol: str
        :param twap_id: int
        :param vaultAddress: str
        :param expireAfter: int
        """
        action = {
            "type": Trade.TWAPCANCEL,
            "a": json.loads(self.ptm.get_exchange_symbol(Common.HYPERLIQUID, product_symbol))[1],
            "t": twap_id,
        }

        payload = {
            "action": action,
            "nonce": "",
            "signature": "",
        }

        if vaultAddress is not None:
            payload["vaultAddress"] = vaultAddress
        if expireAfter is not None:
            payload["expireAfter"] = expireAfter

        res = await self._request(
            method="POST",
            path=Path.EXCHANGE,
            query=payload,
            signed=True,
        )
        return res
