from ._http_manager import HTTPManager
from .endpoint.trade import Trade


class TradeHTTP(HTTPManager):
    def place_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.PLACE_ORDER,
            query=kwargs,
        )

    def place_multiple_orders(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.BATCH_ORDERS,
            query=kwargs,
        )

    def cancel_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CANCEL_ORDER,
            query=kwargs,
        )

    def cancel_multiple_orders(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CANCEL_BATCH_ORDERS,
            query=kwargs,
        )

    def amend_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.AMEND_ORDER,
            query=kwargs,
        )

    def amend_multiple_orders(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.AMEND_BATCH_ORDER,
            query=kwargs,
        )

    def close_positions(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CLOSE_POSITION,
            query=kwargs,
        )

    def get_order(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDER_INFO,
            query=kwargs,
        )

    def get_order_list(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDERS_PENDING,
            query=kwargs,
        )

    def get_orders_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDERS_HISTORY,
            query=kwargs,
        )

    def get_orders_history_archive(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDERS_HISTORY_ARCHIVE,
            query=kwargs,
        )

    def get_fills(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDER_FILLS,
            query=kwargs,
        )

    def place_algo_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.PLACE_ALGO_ORDER,
            query=kwargs,
        )

    def cancel_algo_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CANCEL_ALGOS,
            query=kwargs,
        )

    def cancel_advance_algos(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.Cancel_Advance_Algos,
            query=kwargs,
        )

    def order_algos_list(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDERS_ALGO_PENDING,
            query=kwargs,
        )

    def order_algos_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDERS_ALGO_HISTORY,
            query=kwargs,
        )

    def get_fills_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ORDERS_FILLS_HISTORY,
            query=kwargs,
        )

    def get_easy_convert_currency_list(self):
        return self._request(method="GET", path=Trade.EASY_CONVERT_CURRENCY_LIST)

    def easy_convert(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.EASY_CONVERT,
            query=kwargs,
        )

    def get_easy_convert_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.CONVERT_EASY_HISTORY,
            query=kwargs,
        )

    def get_oneclick_repay_list(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ONE_CLICK_REPAY_SUPPORT,
            query=kwargs,
        )

    def oneclick_repay(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.ONE_CLICK_REPAY,
            query=kwargs,
        )

    def oneclick_repay_history(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ONE_CLICK_REPAY_HISTORY,
            query=kwargs,
        )

    def mass_cancel(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.MASS_CANCEL,
            query=kwargs,
        )

    def mass_all_cancel(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.CANCEL_ALL_AFTER,
            query=kwargs,
        )

    def get_account_rate_limit(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.ACCOUNT_RATE_LIMIT,
            query=kwargs,
        )

    def order_precheck(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.ORDER_PRECHECK,
            query=kwargs,
        )

    def get_algo_order_details(self, **kwargs):
        return self._request(
            method="GET",
            path=Trade.GET_ALGO_ORDER_DETAILS,
            query=kwargs,
        )

    def amend_algo_order(self, **kwargs):
        return self._request(
            method="POST",
            path=Trade.AMEND_ALGO_ORDER,
            query=kwargs,
        )
