from ._http_manager import HTTPManager
from .endpoints.asset import Asset


class AssetHTTP(HTTPManager):
    def get_currencies(
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

        res = self._request(
            method="GET",
            path=Asset.CURRENCY_INFO,
            query=payload,
        )
        return res

    def get_balances(
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

        res = self._request(
            method="GET",
            path=Asset.GET_BALANCES,
            query=payload,
        )
        return res

    def get_asset_valuation(
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

        res = self._request(
            method="GET",
            path=Asset.ASSET_VALUATION,
            query=payload,
        )
        return res

    def funds_transfer(
        self,
        ccy: str,
        amt: str,
        from_account: str,
        to_account: str,
        type: str = None,
        subAcct: str = None,
        loanTrans: str = None,
    ):
        """
        :param ccy: str
        :param amt: str
        :param from_account: str
        :param to_account: str
        :param type: str
        :param subAcct: str
        :param loanTrans: str
        """
        account_map = {
            "FUND": "6",
            "TRADING": "18",
        }

        payload = {
            "ccy": ccy,
            "amt": amt,
            "from": account_map.get(from_account),
            "to": account_map.get(to_account),
        }

        if type is not None:
            payload["type"] = type
        if subAcct is not None:
            payload["subAcct"] = subAcct
        if loanTrans is not None:
            payload["loanTrans"] = loanTrans

        res = self._request(
            method="POST",
            path=Asset.FUNDS_TRANSFER,
            query=payload,
        )
        return res

    def get_transfer_state(
        self,
        transId: str = None,
        clientId: str = None,
        type: str = None,
    ):
        """
        :param transId: str
        :param clientId: str
        :param type: str
        """
        payload = {}
        if transId is not None:
            payload["transId"] = transId
        if clientId is not None:
            payload["clientId"] = clientId
        if type is not None:
            payload["type"] = type

        res = self._request(
            method="GET",
            path=Asset.TRANSFER_STATE,
            query=payload,
        )
        return res

    def get_bills(
        self,
        type: str = None,
        clientId: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param type: str
        :param clientId: str
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {}
        if type is not None:
            payload["type"] = type
        if clientId is not None:
            payload["clientId"] = clientId
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Asset.BILLS_INFO,
            query=payload,
        )
        return res

    def get_deposit_address(
        self,
        ccy: str,
    ):
        """
        :param ccy: str
        """
        payload = {
            "ccy": ccy,
        }

        res = self._request(
            method="GET",
            path=Asset.DEPOSIT_ADDRESS,
            query=payload,
        )
        return res

    def get_deposit_history(
        self,
        ccy: str = None,
        depId: str = None,
        fromWdId: str = None,
        txId: str = None,
        type: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param ccy: str
        :param depId: str
        :param fromWdId: str
        :param txId: str
        :param type: str
        :param state: str
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {}
        if ccy is not None:
            payload["ccy"] = ccy
        if depId is not None:
            payload["depId"] = depId
        if fromWdId is not None:
            payload["fromWdId"] = fromWdId
        if txId is not None:
            payload["txId"] = txId
        if type is not None:
            payload["type"] = type
        if state is not None:
            payload["state"] = state
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Asset.DEPOSIT_HISTORY,
            query=payload,
        )
        return res

    def withdrawal(
        self,
        ccy: str,
        amt: str,
        dest: str,
        toAddr: str,
        chain: str = None,
        areaCode: str = None,
        rcvrInfo: str = None,
    ):
        """
        :param ccy: str
        :param amt: str
        :param dest: str
        :param toAddr: str
        :param chain: str
        :param areaCode: str
        :param rcvrInfo: str
        """
        payload = {
            "ccy": ccy,
            "amt": amt,
            "dest": dest,
            "toAddr": toAddr,
        }
        if chain is not None:
            payload["chain"] = chain
        if areaCode is not None:
            payload["areaCode"] = areaCode
        if rcvrInfo is not None:
            payload["rcvrInfo"] = rcvrInfo

        res = self._request(
            method="POST",
            path=Asset.WITHDRAWAL_COIN,
            query=payload,
        )
        return res

    def cancel_withdrawal(
        self,
        wdId: str,
    ):
        """
        :param wdId: str
        """
        payload = {
            "wdId": wdId,
        }

        res = self._request(
            method="POST",
            path=Asset.CANCEL_WITHDRAWAL,
            query=payload,
        )
        return res

    def get_withdrawal_history(
        self,
        ccy: str = None,
        wdId: str = None,
        clientId: str = None,
        txId: str = None,
        type: str = None,
        state: str = None,
        after: str = None,
        before: str = None,
        limit: str = None,
    ):
        """
        :param ccy: str
        :param wdId: str
        :param clientId: str
        :param txId: str
        :param type: str
        :param state: str
        :param after: str
        :param before: str
        :param limit: str
        """
        payload = {}
        if ccy is not None:
            payload["ccy"] = ccy
        if wdId is not None:
            payload["wdId"] = wdId
        if clientId is not None:
            payload["clientId"] = clientId
        if txId is not None:
            payload["txId"] = txId
        if type is not None:
            payload["type"] = type
        if state is not None:
            payload["state"] = state
        if after is not None:
            payload["after"] = after
        if before is not None:
            payload["before"] = before
        if limit is not None:
            payload["limit"] = limit

        res = self._request(
            method="GET",
            path=Asset.WITHDRAWAL_HISTORY,
            query=payload,
        )
        return res

    def get_deposit_withdraw_status(
        self,
        wdId: str = None,
        txId: str = None,
        ccy: str = None,
        to: str = None,
        chain: str = None,
    ):
        """
        :param wdId: str
        :param txId: str
        :param ccy: str
        :param to: str
        :param chain: str
        """
        payload = {}
        if wdId is not None:
            payload["wdId"] = wdId
        if txId is not None:
            payload["txId"] = txId
        if ccy is not None:
            payload["ccy"] = ccy
        if to is not None:
            payload["to"] = to
        if chain is not None:
            payload["chain"] = chain

        res = self._request(
            method="GET",
            path=Asset.GET_DEPOSIT_WITHDRAW_STATUS,
            query=payload,
        )
        return res

    def get_exchange_list(self):
        res = self._request(
            method="GET",
            path=Asset.EXCHANGE_LIST,
            query=None,
        )
        return res

    def post_monthly_statement(
        self,
        month: str = None,
    ):
        """
        :param month: str (Jan)
        """
        payload = {}
        if month is not None:
            payload["month"] = month

        res = self._request(
            method="POST",
            path=Asset.MONTHLY_STATEMENT,
            query=payload,
        )
        return res

    def get_monthly_statement(
        self,
        month: str,
    ):
        """
        :param month: str (Jan)
        """
        payload = {
            "month": month,
        }

        res = self._request(
            method="GET",
            path=Asset.MONTHLY_STATEMENT,
            query=payload,
        )
        return res

    def get_convert_currencies(self):
        res = self._request(
            method="GET",
            path=Asset.GET_CURRENCIES,
            query=None,
        )
        return res
