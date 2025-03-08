from ._http_manager import HTTPManager
from .endpoint.trade import Trade


class TradeHTTP(HTTPManager):
    def place_order(self, **kwargs):
        return self._request("POST", Trade.PLACE_ORDER, kwargs)

    def place_multiple_orders(self, orders_data):
        return self._request("POST", Trade.BATCH_ORDERS, orders_data)

    def cancel_order(self, **kwargs):
        return self._request("POST", Trade.CANCEL_ORDER, kwargs)

    def cancel_multiple_orders(self, orders_data):
        return self._request("POST", Trade.CANCEL_BATCH_ORDERS, orders_data)

    def amend_order(self, **kwargs):
        return self._request("POST", Trade.AMEND_ORDER, kwargs)

    def amend_multiple_orders(self, orders_data):
        return self._request("POST", Trade.AMEND_BATCH_ORDER, orders_data)

    def close_positions(self, **kwargs):
        return self._request("POST", Trade.CLOSE_POSITION, kwargs)

    def get_order(self, **kwargs):
        return self._request("GET", Trade.ORDER_INFO, kwargs)

    def get_order_list(self, **kwargs):
        return self._request("GET", Trade.ORDERS_PENDING, kwargs)

    def get_orders_history(self, **kwargs):
        return self._request("GET", Trade.ORDERS_HISTORY, kwargs)

    def get_orders_history_archive(self, **kwargs):
        return self._request("GET", Trade.ORDERS_HISTORY_ARCHIVE, kwargs)

    def get_fills(self, **kwargs):
        return self._request("GET", Trade.ORDER_FILLS, kwargs)

    def place_algo_order(self, **kwargs):
        return self._request("POST", Trade.PLACE_ALGO_ORDER, kwargs)

    def cancel_algo_order(self, **kwargs):
        return self._request("POST", Trade.CANCEL_ALGOS, kwargs)

    def cancel_advance_algos(self, **kwargs):
        return self._request("POST", Trade.Cancel_Advance_Algos, kwargs)

    def order_algos_list(self, **kwargs):
        return self._request("GET", Trade.ORDERS_ALGO_PENDING, kwargs)

    def order_algos_history(self, **kwargs):
        return self._request("GET", Trade.ORDERS_ALGO_HISTORY, kwargs)

    def get_fills_history(self, **kwargs):
        return self._request("GET", Trade.ORDERS_FILLS_HISTORY, kwargs)

    def get_easy_convert_currency_list(self):
        return self._request("GET", Trade.EASY_CONVERT_CURRENCY_LIST)

    def easy_convert(self, **kwargs):
        return self._request("POST", Trade.EASY_CONVERT, kwargs)

    def get_easy_convert_history(self, **kwargs):
        return self._request("GET", Trade.CONVERT_EASY_HISTORY, kwargs)

    def get_oneclick_repay_list(self, **kwargs):
        return self._request("GET", Trade.ONE_CLICK_REPAY_SUPPORT, kwargs)

    def oneclick_repay(self, **kwargs):
        return self._request("POST", Trade.ONE_CLICK_REPAY, kwargs)

    def oneclick_repay_history(self, **kwargs):
        return self._request("GET", Trade.ONE_CLICK_REPAY_HISTORY, kwargs)

    def get_algo_order_details(self, **kwargs):
        return self._request("GET", Trade.GET_ALGO_ORDER_DETAILS, kwargs)

    def amend_algo_order(self, **kwargs):
        return self._request("POST", Trade.AMEND_ALGO_ORDER, kwargs)
