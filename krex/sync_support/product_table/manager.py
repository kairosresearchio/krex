import asyncio
import pandas as pd
from contextlib import asynccontextmanager
from .fetch import bitmart

VALID_EXCHANGES = [
    # bybit,
    # okx,
    bitmart,
]


class ProductTableError(Exception):
    pass


class ProductTableManager:
    """
    Exchange Product Mapping Table

    This table provides a structured mapping between product symbols and their corresponding exchange-specific symbols,
    along with key trading attributes. It helps standardize the representation of products across different exchanges.

    Columns:
        - product_symbol: Standardized product identifier used internally.
        - exchange_symbol: The product symbol as recognized on the exchange.
        - exchange: The name of the exchange where the product is traded.
        - product_type: The category of the product (e.g., SPOT, SWAP, FUTURES).
        - price_precision: The decimal precision allowed for price values (if applicable).
        - size_precision: The decimal precision allowed for order sizes (if applicable).
        - contract_value: The notional value of one contract (for derivatives).
        - min_size: The minimum order size allowed on the exchange.
        - min_notional: The minimum notional value required for an order.

    Example:
        | product_symbol  | exchange_symbol | exchange | product_type | price_precision | size_precision | contract_value | min_size | min_notional |
        |-----------------|-----------------|----------|--------------|-----------------|----------------|----------------|----------|--------------|
        | BTC-USDT-SPOT   | BTC/USDT        | BINANCE  | SPOT         | 0.01            | 0.0001         | N/A            | 0.0001   | 10           |
        | BTC-USD-SWAP    | BTCUSDT         | BINANCE  | SWAP         | 0.1             | 0.001          | 100 USD        | 0.001    | 5            |
        | BTC-USD-FUTURES | BTC-USD-SWAP    | OKX      | FUTURES      | 0.01            | 0.0001         | 10 USD         | 0.0001   | 1            |

    Use this mapping to correctly interpret product symbols and their attributes when integrating with multiple exchanges.
    """

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            asyncio.run(cls._instance._initialize())
        return cls._instance

    async def _initialize(self):
        """Initialize the product table by fetching data from valid exchanges."""
        self.product_table = await self._fetch_product_tables()

    async def _fetch_product_tables(self):
        """Fetch product tables from all valid exchanges and combine them into a single DataFrame."""
        product_tables = await asyncio.gather(*[func() for func in VALID_EXCHANGES])
        return pd.concat(product_tables, ignore_index=True)

    @asynccontextmanager
    async def _create_exchange_clients(self):
        """Create exchange clients as an async context manager to ensure proper cleanup."""
        clients = [exchange() for exchange in VALID_EXCHANGES]
        try:
            yield clients
        finally:
            await asyncio.gather(*[client.close() for client in clients if hasattr(client, "close")])

    def get(
        self,
        key,
        product_symbol=None,
        exchange=None,
        product_type=None,
        exchange_symbol=None,
    ):
        """
        Return a array of values of key from product that satisfy the conditions.
        The conditions are case-insensitive (except id_).
        """
        data = self.product_table
        if product_symbol is not None:
            data = data[data["product_symbol"] == product_symbol]
        if exchange is not None:
            data = data[data["exchange"] == exchange]
        if product_type is not None:
            data = data[data["product_type"] == product_type]
        if exchange_symbol is not None:
            data = data[data["exchange_symbol"] == exchange_symbol]

        if len(data) > 1:
            raise ProductTableError(
                "Exist multiple {} for product_code: {}, exchange: {}, product_type: {}".format(
                    key, product_symbol, exchange, product_type
                )
            )
        if len(data) == 0:
            raise ProductTableError(
                "Not exist {} for product_code: {}, exchange: {}, product_type: {}, exchange_symbol: {}".format(
                    key, product_symbol, exchange, product_type, exchange_symbol
                )
            )
        return data.iloc[0][key]

    def get_exchange_symbol(self, product_symbol, exchange):
        return self.get("exchange_symbol", product_symbol, exchange)

    def get_product_symbol(self, exchange_symbol, exchange):
        return self.get("product_symbol", exchange_symbol=exchange_symbol, exchange=exchange)

    def get_product_type(self, product_symbol, exchange):
        return self.get("product_type", product_symbol, exchange)

    def get_base_currency(self, product_symbol, exchange):
        return self.get("base_currency", product_symbol, exchange)

    def get_quote_currency(self, product_symbol, exchange):
        return self.get("quote_currency", product_symbol, exchange)

    def get_trading_details(self, product_symbol, exchange):
        return {
            "price_precision": self.get("price_precision", product_symbol, exchange),
            "size_precision": self.get("size_precision", product_symbol, exchange),
            "min_size": self.get("min_size", product_symbol, exchange),
            "min_notional": self.get("min_notional", product_symbol, exchange),
            "size_per_contract": self.get("size_per_contract", product_symbol, exchange),
        }
