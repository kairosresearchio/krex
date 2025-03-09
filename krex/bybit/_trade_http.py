from ._http_manager import HTTPManager
from .endpoints.trade import Trade


class TradeHTTP(HTTPManager):
    def place_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.PLACE_ORDER,
            query=kwargs,
        )

    def amend_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.AMEND_ORDER,
            query=kwargs,
        )

    def cancel_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CANCEL_ORDER,
            query=kwargs,
        )

    def get_open_orders(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.GET_OPEN_ORDERS,
            query=kwargs,
        )

    def cancel_all_orders(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CANCEL_ALL_ORDERS,
            query=kwargs,
        )

    def get_order_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.GET_ORDER_HISTORY,
            query=kwargs,
        )

    def place_batch_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.BATCH_PLACE_ORDER,
            query=kwargs,
        )

    def amend_batch_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.BATCH_AMEND_ORDER,
            query=kwargs,
        )

    def cancel_batch_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.BATCH_CANCEL_ORDER,
            query=kwargs,
        )

    def get_borrow_quota(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.GET_BORROW_QUOTA,
            query=kwargs,
        )

    def set_dcp(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.SET_DCP,
            query=kwargs,
        )
