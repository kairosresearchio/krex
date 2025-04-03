from ..utils.common import Common
from ._http_manager import HTTPManager
from .endpoints.trade import Trade



class TradeHTTP(HTTPManager):
    def add_order(
        self,
        nonce: int,  # Nonce used in construction of API-Sign header
        cl_ord_id: str,  # Required: Adds an alphanumeric client order identifier which uniquely identifies an open order for each client
        ordertype: str,  # Required: Execution model of the order (e.g., market, limit, etc.)
        type: str,  # Required: Order direction (buy/sell)
        volume: str,  # Required: Order quantity in terms of the base asset
        pair: str,  # Required: Asset pair id or altname
        price: str,  # Required: Limit price for limit and iceberg orders, Trigger price for stop-loss and other orders
        trigger: str,  # Required: Price signal used to trigger stop-loss, take-profit, etc.
        close: str,  # Required: Close order type
        deadline: str,  # Required: Timestamp after which matching engine should reject order
        validate: bool,  # Required: If true, order will be validated only
        # Optional arguments with default values
        userref: int = None,  # Optional: Non-unique identifier
        displayvol: str = None,  # Optional: For iceberg orders only
        price2: str = None,  # Optional: Secondary price for stop-loss-limit, etc.
        leverage: str = None,  # Optional: Amount of leverage desired
        reduce_only: bool = None,  # Optional: If true, order will only reduce open positions
        stptype: str = None,  # Optional: Self Trade Prevention
        oflags: str = None,  # Optional: Comma delimited list of order flags
        timeinforce: str = None,  # Optional: Time-In-Force (default: GTC)
        starttm: str = None,  # Optional: Scheduled start time
        expiretm: str = None,  # Optional: Expiry time for GTD orders
    ):
        """
        Sends a single, new order into the exchange with various order types, time-in-force, and flags.
        """
        payload = {
            "nonce": nonce,
            "userref": userref,
            "cl_ord_id": cl_ord_id,
            "ordertype": ordertype,
            "type": type,
            "volume": volume,
            "displayvol": displayvol,
            "pair": pair,
            "price": price,
            "price2": price2,
            "trigger": trigger,
            "leverage": leverage,
            "reduce_only": reduce_only,
            "stptype": stptype,
            "oflags": oflags,
            "timeinforce": timeinforce,
            "starttm": starttm,
            "expiretm": expiretm,
            "close": close,
            "deadline": deadline,
            "validate": validate
        }
        
        # Remove None values to keep request clean
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.http._request(
            method="POST",
            endpoint=str(Trade.ADD_ORDER),
            data=payload,
            auth=True
        )
    
    def add_order_batch(
        self,
        nonce: int,
        orders: list,
        pair: str,
        deadline: str,
        validate: bool = False
    ):
        """
        Places a batch of orders (minimum of 2 and maximum 15):
        Validation is performed on the whole batch prior to submission to the engine. If an order fails validation, the whole batch will be rejected.
        On submission to the engine, if an order fails pre-match checks (i.e. funding), then the individual order will be rejected and remainder of the batch will be processed.
        All orders in batch are limited to a single pair.
        """
        payload = {
            "nonce": nonce,
            "orders": orders,
            "pair": pair,
            "deadline": deadline,
            "validate": validate
        }
        
        return self.http._request(
            method="POST",
            endpoint=str(Trade.ADD_ORDER_BATCH),
            data=payload,
            auth=True
        )

    def amend_order(
        self,
        nonce: int,
        txid: str = None,
        cl_ord_id: str = None,
        order_qty: str = None,
        display_qty: str = None,
        limit_price: str = None,
        trigger_price: str = None,
        post_only: bool = None,
        deadline: str = None
    ):
        """Amends an existing order."""
        payload = {
            "nonce": nonce,
            "txid": txid,
            "cl_ord_id": cl_ord_id,
            "order_qty": order_qty,
            "display_qty": display_qty,
            "limit_price": limit_price,
            "trigger_price": trigger_price,
            "post_only": post_only,
            "deadline": deadline
        }
        
        # Remove None values to keep request clean
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.http._request(
            method="POST",
            endpoint=str(Trade.AMEND_ORDER),
            data=payload,
            auth=True
        )
    
    def cancel_order(
        self,
        nonce: int, 
        txid: str = None, 
        cl_ord_id: str = None
    ):
        """Cancels a specific order by txid or cl_ord_id."""
        payload = {
            "nonce": nonce,
            "txid": txid,
            "cl_ord_id": cl_ord_id
        }

        # Remove None values to keep request clean
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.http._request(
            method="POST",
            endpoint=str(Trade.CANCEL_ORDER),
            data=payload,
            auth=True
        )
    
    def cancel_all_orders(
        self, 
        nonce: int
    ):
        """Cancels all open orders."""
        payload = {"nonce": nonce}

        return self.http._request(
            method="POST",
            endpoint=str(Trade.CANCEL_ALL_ORDERS),
            data=payload,
            auth=True
        )

    def cancel_all_orders_after(
            self, 
            nonce: int, 
            timeout: int
    ):
        """Sets a Dead Man's Switch to cancel all orders after the given timeout (in seconds)."""
        payload = {
            "nonce": nonce,
            "timeout": timeout
        }

        return self.http._request(
            method="POST",
            endpoint=str(Trade.CANCEL_ALL_ORDERS_AFTER),
            data=payload,
            auth=True
        )
    def cancel_order_batch(
            self, 
            nonce: int, 
            orders: list = None, 
            cl_ord_ids: list = None
    ):
        """Cancels multiple open orders by txid or client order ID (max 50 total)."""
        if not orders and not cl_ord_ids:
            raise ValueError("At least one of 'orders' or 'cl_ord_ids' must be provided.")

        if orders and len(orders) > 50:
            raise ValueError("Maximum 50 order txids allowed.")
        
        if cl_ord_ids and len(cl_ord_ids) > 50:
            raise ValueError("Maximum 50 client order IDs allowed.")

        payload = {
            "nonce": nonce,
            "orders": orders or [],
            "cl_ord_ids": cl_ord_ids or []
        }

        return self.http._request(
            method="POST",
            endpoint=str(Trade.CANCEL_ORDER_BATCH),
            data=payload,
            auth=True
        )
    
    def get_websockets_token(
        self,
        nonce: int
    ):
        """Retrieves an authentication token for Kraken WebSockets API."""
        payload = {"nonce": nonce}

        return self.http._request(
            method="POST",
            endpoint=str(Trade.GET_WEBSOCKETS_TOKEN),
            data=payload,
            auth=True
        )
