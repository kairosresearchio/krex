import pandas as pd
import asyncio
from contextlib import asynccontextmanager
from krex.product_table.fetch import bybit, okx, bitmart

VALID_EXCHANGES = [
    bybit,
    okx,
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

    async def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            await cls._instance._initialize()
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

    def construct_product_code(self, base_currency, currency, product_type):
        """
        Construct product_code from base_currency, currency, product_type
        base_currency: BTC, ETH,
        currency: USDT, USD, ...
        product_type: SPOT, UPERP, ...
        """
        product_type = product_type.upper()
        return "{}-{}-{}".format(base_currency, currency, product_type)

    def get_exchange_symbol(self, product_symbol, exchange):
        return self.get("exchange_symbol", product_symbol, exchange)

    def get_product_symbol(self, exchange_symbol, exchange):
        return self.get("product_symbol", exchange_symbol=exchange_symbol, exchange=exchange)

    def get_product_type(self, product_symbol, exchange):
        return self.get("product_type", product_symbol, exchange)

    def convert_product_type(self, product_code, from_product_type, to_product_type):
        base, quote, product_type = product_code.split("-")
        if to_product_type == "SPOT":
            return "{}-{}-SPOT".format(base, quote)
        elif to_product_type == "UPERP":
            return "{}-{}-UPERP".format(base, quote)
