from ._http_manager import HTTPManager
from .endpoints.account import Account
from ...utils.common import Common


class AccountHTTP(HTTPManager):
    async def get_account_instruments(
        self,
        instType: str,
        product_symbol: str = None,
        instFamily: str = None,
        uly: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param product_symbol: str Only applicable to FUTURES/SWAP/OPTION.If instType is OPTION, either uly or instFamily is required.
        :param instFamily: str Only applicable to FUTURES/SWAP/OPTION. If instType is OPTION, either uly or instFamily is required.
        :param uly: str
        """
        payload = {
            "instType": instType,
        }
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if uly is not None:
            payload["uly"] = uly

        res = await self._request(
            method="GET",
            path=Account.GET_INSTRUMENTS,
            query=payload,
        )
        return res

    async def get_account_balance(
        self,
        ccy: str = None,
    ):
        """
        :param ccy: str
        """
        payload = {}
        if ccy is not None:
            coinName = ",".join(ccy)
            payload = {
                "ccy": coinName,
            }

        res = await self._request(
            method="GET",
            path=Account.ACCOUNT_INFO,
            query=payload,
        )
        return res

    async def get_positions(
        self,
        instType: str = None,
        product_symbol: str = None,
    ):
        """
        :param instType: str (MARGIN, SWAP, FUTURES, OPTION) instId will be checked against instType when both parameters are passed.
        :param product_symbol: str
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)

        res = await self._request(
            method="GET",
            path=Account.POSITION_INFO,
            query=payload,
        )
        return res

    async def get_positions_history(
        self,
        instType: str = None,
        product_symbol: str = None,
        mgnMode: str = None,
        type: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (MARGIN, SWAP, FUTURES, OPTION)
        :param product_symbol: str
        :param mgnMode: str (cross, isolated)
        :param type: str (1: Close position partially; 2: Close all; 3: Liquidation; 4: Partial liquidation; 5: ADL;)
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if mgnMode is not None:
            payload["mgnMode"] = mgnMode
        if type is not None:
            payload["type"] = type
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Account.POSITIONS_HISTORY,
            query=payload,
        )
        return res

    async def get_position_risk(
        self,
        instType: str = None,
    ):
        """
        :param instType: str (MARGIN, SWAP, FUTURES, OPTION)
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType

        res = await self._request(
            method="GET",
            path=Account.POSITION_RISK,
            query=payload,
        )
        return res

    async def get_account_bills(
        self,
        instType: str = None,
        product_symbol: str = None,
        ccy: str = None,
        mgnMode: str = None,
        ctType: str = None,
        type: str = None,
        subType: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param product_symbol: str
        :param ccy: str
        :param mgnMode: str (cross, isolated)
        :param ctType: str
        :param type: str
        :param subType: str
        :param begin: str
        :param end: str
        :param limit: str
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ccy is not None:
            payload["ccy"] = ccy
        if mgnMode is not None:
            payload["mgnMode"] = mgnMode
        if ctType is not None:
            payload["ctType"] = ctType
        if type is not None:
            payload["type"] = type
        if subType is not None:
            payload["subType"] = subType
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Account.BILLS_DETAIL,
            query=payload,
        )
        return res

    async def get_account_bills_archive(
        self,
        instType: str = None,
        product_symbol: str = None,
        ccy: str = None,
        mgnMode: str = None,
        ctType: str = None,
        type: str = None,
        subType: str = None,
        begin: str = None,
        end: str = None,
        limit: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param product_symbol: str
        :param ccy: str
        :param mgnMode: str (cross, isolated)
        :param ctType: str
        :param type: str
        :param subType: str
        :param begin: str
        :param end: str
        :param limit: str
        """
        payload = {}
        if instType is not None:
            payload["instType"] = instType
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ccy is not None:
            payload["ccy"] = ccy
        if mgnMode is not None:
            payload["mgnMode"] = mgnMode
        if ctType is not None:
            payload["ctType"] = ctType
        if type is not None:
            payload["type"] = type
        if subType is not None:
            payload["subType"] = subType
        if begin is not None:
            payload["begin"] = begin
        if end is not None:
            payload["end"] = end
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Account.BILLS_ARCHIVE,
            query=payload,
        )
        return res

    async def get_account_bills_history_archive(
        self,
        year: str,
        quarter: str,
    ):
        """
        :param year: str
        :param quarter: str
        """
        payload = {
            "year": year,
            "quarter": quarter,
        }

        res = await self._request(
            method="GET",
            path=Account.BILLS_HISTORY_ARCHIVE,
            query=payload,
        )
        return res

    async def post_account_bills_history_archive(
        self,
        year: str,
        quarter: str,
    ):
        """
        :param year: str
        :param quarter: str
        """
        payload = {
            "year": year,
            "quarter": quarter,
        }

        res = await self._request(
            method="POST",
            path=Account.BILLS_HISTORY_ARCHIVE,
            query=payload,
        )
        return res

    async def get_account_config(self):
        res = await self._request(
            method="GET",
            path=Account.ACCOUNT_CONFIG,
            query=None,
        )
        return res

    async def set_position_mode(self, posMode: str):
        """
        :param posMode: str (long_short_mode)
        """
        payload = {
            "posMode": posMode,
        }

        res = await self._request(
            method="POST",
            path=Account.POSITION_MODE,
            query=payload,
        )
        return res

    async def set_leverage(
        self,
        lever: str,
        mgnMode: str,
        product_symbol: str = None,
        ccy: str = None,
        posSide: str = None,
    ):
        """
        :param lever: str
        :param mgnMode: str (cross, isolated), Can only be cross if ccy is passed.
        :param product_symbol: str Under cross mode, either instId or ccy is required; if both are passed, instId will be used by async default.
        :param ccy: str Only applicable to cross MARGIN of Spot mode/Multi-currency margin/Portfolio margin
        :param posSide: str Only required when margin mode is isolated in long/short mode for FUTURES/SWAP.
        """
        payload = {
            "lever": lever,
            "mgnMode": mgnMode,
        }
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ccy is not None:
            payload["ccy"] = ccy
        if posSide is not None:
            payload["posSide"] = posSide

        res = await self._request(
            method="POST",
            path=Account.SET_LEVERAGE,
            query=payload,
        )
        return res

    async def get_max_order_size(
        self,
        product_symbol: str,
        tdMode: str,
        ccy: str = None,
        px: str = None,
        leverage: str = None,
    ):
        """
        :param product_symbol: str
        :param tdMode: str (cross, isolated, cash, spot_isolated)
        :param ccy: str Currency used for margin Applicable to isolated MARGIN and cross MARGIN orders in Spot and futures mode.
        :param px: str
        :param leverage: str
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
            "tdMode": tdMode,
        }
        if ccy is not None:
            payload["ccy"] = ccy
        if px is not None:
            payload["px"] = px
        if leverage is not None:
            payload["leverage"] = leverage

        res = await self._request(
            method="GET",
            path=Account.MAX_TRADE_SIZE,
            query=payload,
        )
        return res

    async def get_max_avail_size(
        self,
        product_symbol: str,
        tdMode: str,
        ccy: str = None,
        reduceOnly: str = None,
        px: str = None,
    ):
        """
        :param product_symbol: str
        :param tdMode: str (cross, isolated, cash, spot_isolated)
        :param ccy: str Applicable to isolated MARGIN and cross MARGIN in Spot and futures mode.
        :param reduceOnly: str Whether to reduce position only Only applicable to MARGIN
        :param px: str Only applicable to reduceOnly MARGIN.
        """
        payload = {
            "instId": self.ptm.get_exchange_symbol(Common.OKX, product_symbol),
            "tdMode": tdMode,
        }
        if ccy is not None:
            payload["ccy"] = ccy
        if reduceOnly is not None:
            payload["reduceOnly"] = reduceOnly
        if px is not None:
            payload["px"] = px

        res = await self._request(
            method="GET",
            path=Account.MAX_AVAIL_SIZE,
            query=payload,
        )
        return res

    async def get_leverage(
        self,
        mgnMode: str,
        product_symbol: str = None,
        ccy: str = None,
    ):
        """
        :param mgnMode: str (cross, isolated)
        :param product_symbol: str
        :param ccy: str used for getting leverage of currency level. Applicable to cross MARGIN of Spot mode/Multi-currency margin/Portfolio margin. Supported single currency or multiple currencies (no more than 20) separated with comma.
        """
        payload = {
            "mgnMode": mgnMode,
        }
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ccy is not None:
            payload["ccy"] = ccy

        res = await self._request(
            method="GET",
            path=Account.GET_LEVERAGE,
            query=payload,
        )
        return res

    async def get_adjust_leverage(
        self,
        instType: str,
        mgnMode: str,
        lever: str,
        product_symbol: str = None,
        ccy: str = None,
        posSide: str = None,
    ):
        """
        :param instType: str (MARGIN, SWAP, FUTURES)
        :param mgnMode: str (cross, isolated)
        :param lever: str
        :param product_symbol: str
        :param ccy: str
        :param posSide: str (long, short)
        """
        payload = {
            "instType": instType,
            "mgnMode": mgnMode,
            "lever": lever,
        }
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if ccy is not None:
            payload["ccy"] = ccy
        if posSide is not None:
            payload["posSide"] = posSide

        res = await self._request(
            method="GET",
            path=Account.GET_ADJUST_LEVERAGE,
            query=payload,
        )
        return res

    async def get_max_loan(
        self,
        mgnMode: str,
        product_symbol: str = None,
        ccy: str = None,
        mgnCcy: str = None,
    ):
        """
        :param mgnMode: str (cross, isolated)
        :param product_symbol: str
        :param ccy: str
        :param mgnCcy: str
        """
        payload = {
            "mgnMode": mgnMode,
        }
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(product_symbol, Common.OKX)
        if ccy is not None:
            payload["ccy"] = ccy
        if mgnCcy is not None:
            payload["mgnCcy"] = mgnCcy

        res = await self._request(
            method="GET",
            path=Account.MAX_LOAN,
            query=payload,
        )
        return res

    async def get_fee_rates(
        self,
        instType: str,
        ruleType: str = None,
        product_symbol: str = None,
        uly: str = None,
        instFamily: str = None,
    ):
        """
        :param instType: str (SPOT, MARGIN, SWAP, FUTURES, OPTION)
        :param ruleType: str Trading rule types normal: normal trading pre_market: pre-market trading ruleType can not be passed through together with product_symbol/instFamily/uly
        :param product_symbol: str
        :param uly: str
        :param instFamily: str
        """
        payload = {
            "instType": instType,
        }
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if uly is not None:
            payload["uly"] = uly
        if instFamily is not None:
            payload["instFamily"] = instFamily
        if ruleType is not None:
            payload["ruleType"] = ruleType

        res = await self._request(
            method="GET",
            path=Account.FEE_RATES,
            query=payload,
        )
        return res

    async def get_interest_accrued(
        self,
        ccy: str = None,
        product_symbol: str = None,
        mgnMode: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param ccy: str
        :param product_symbol: str
        :param mgnMode: str (cross, isolated)
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {}
        if ccy is not None:
            payload["ccy"] = ccy
        if product_symbol is not None:
            payload["instId"] = self.ptm.get_exchange_symbol(Common.OKX, product_symbol)
        if mgnMode is not None:
            payload["mgnMode"] = mgnMode
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        res = await self._request(
            method="GET",
            path=Account.INTEREST_ACCRUED,
            query=payload,
        )
        return res

    async def get_interest_rate(
        self,
        ccy: str = None,
    ):
        """
        :param ccy: str
        """
        payload = {}
        if ccy is not None:
            payload["ccy"] = ccy

        res = await self._request(
            method="GET",
            path=Account.INTEREST_RATE,
            query=payload,
        )
        return res

    async def set_greeks(
        self,
        greeksType: str,
    ):
        """
        :param greeksType: str PA: Greeks in coins, BS: Black-Scholes Greeks in dollars
        """
        payload = {
            "greeksType": greeksType,
        }

        res = await self._request(
            method="POST",
            path=Account.SET_GREEKS,
            query=payload,
        )
        return res

    async def set_isolated_mode(
        self,
        type: str,
    ):
        """
        :param type: str (MARGIN, CONTRACTS)
        """
        payload = {
            "isoMode": "automatic",
            "type": type,
        }

        res = await self._request(
            method="POST",
            path=Account.SET_ISOLATED_MODE,
            query=payload,
        )
        return res

    async def get_max_withdrawal(
        self,
        ccy: str = None,
    ):
        """
        :param ccy: str
        """
        payload = {}
        if ccy is not None:
            ccyName = ",".join(ccy)
            payload = {
                "ccy": ccyName,
            }

        res = await self._request(
            method="GET",
            path=Account.MAX_WITHDRAWAL,
            query=payload,
        )
        return res

    async def get_interest_limits(
        self,
        ccy: str = None,
    ):
        """
        :param ccy: str
        """
        payload = {}
        if ccy is not None:
            payload["ccy"] = ccy

        res = await self._request(
            method="GET",
            path=Account.INTEREST_LIMITS,
            query=payload,
        )
        return res

    async def set_auto_loan(
        self,
        autoLoan: bool,
    ):
        """
        :param autoLoan: bool
        """
        kwargs = {
            "autoLoan": autoLoan,
        }

        res = await self._request(
            method="POST",
            path=Account.SET_AUTO_LOAN,
            query=kwargs,
        )
        return res
