import asyncio
import polars as pl
from contextlib import asynccontextmanager
from .fetch import bybit, okx, bitmart, gateio, binance, hyperliquid, bingx, kucoin, ascendex, bitmex, zoomex

VALID_EXCHANGES = [
    bybit,
    okx,
    bitmart,
    gateio,
    binance,
    hyperliquid,
    bingx,
    kucoin,
    ascendex,
    bitmex,
    zoomex,
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

    _instance = {}

    @classmethod
    async def get_instance(cls, exchange_name=None):
        if exchange_name not in cls._instance:
            cls._instance[exchange_name] = cls()
            await cls._instance[exchange_name]._initialize(exchange_name=exchange_name)
        return cls._instance[exchange_name]

    async def _initialize(self, exchange_name=None):
        """Initialize the product table by fetching data from valid exchanges."""
        self.product_table = await self._fetch_product_tables(exchange_name)

    async def _fetch_product_tables(self, exchange_name=None):
        """Fetch product tables from all valid exchanges and combine them into a single DataFrame."""
        if exchange_name is None:
            product_tables = await asyncio.gather(*[func() for func in VALID_EXCHANGES])
        else:
            product_tables = await asyncio.gather(
                *[func() for func in VALID_EXCHANGES if func.__name__ == exchange_name]
            )
        return pl.concat(product_tables, how="vertical")

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
        exchange_type=None,
        exchange_symbol=None,
    ):
        """
        Return a array of values of key from product that satisfy the conditions.
        The conditions are case-insensitive (except id_).
        """
        data = self.product_table
        if product_symbol is not None:
            data = data.filter(pl.col("product_symbol") == product_symbol)
        if exchange is not None:
            data = data.filter(pl.col("exchange") == exchange)
        if product_type is not None:
            data = data.filter(pl.col("product_type") == product_type)
        if exchange_type is not None:
            data = data.filter(pl.col("exchange_type") == exchange_type)
        if exchange_symbol is not None:
            data = data.filter(pl.col("exchange_symbol") == exchange_symbol)

        if data.height > 1:
            raise ProductTableError(
                f"Exist multiple {key} for product_symbol: {product_symbol}, exchange: {exchange}, product_type: {product_type}"
            )
        if data.height == 0:
            raise ProductTableError(
                f"Not exist {key} for product_symbol: {product_symbol}, exchange: {exchange}, product_type: {product_type}, exchange_symbol: {exchange_symbol}"
            )

        return data.select(key).item()

    def get_exchange_symbol(self, exchange, product_symbol):
        return self.get("exchange_symbol", product_symbol, exchange)

    def get_product_symbol(self, exchange, exchange_symbol, product_type=None, exchange_type=None):
        if product_type is not None and exchange_type is None:
            return self.get(
                "product_symbol", exchange_symbol=exchange_symbol, exchange=exchange, product_type=product_type
            )
        elif product_type is None and exchange_type is not None:
            return self.get(
                "product_symbol", exchange_symbol=exchange_symbol, exchange=exchange, exchange_type=exchange_type
            )
        elif product_type is not None and exchange_type is not None:
            return self.get(
                "product_symbol",
                exchange_symbol=exchange_symbol,
                exchange=exchange,
                product_type=product_type,
                exchange_type=exchange_type,
            )
        else:
            raise ProductTableError("You must specify either product_type or exchange_type")

    def get_product_type(self, exchange, product_symbol=None, exchange_symbol=None):
        if product_symbol is not None:
            return self.get("product_type", product_symbol=product_symbol, exchange=exchange)
        elif exchange_symbol is not None:
            return self.get("product_type", exchange_symbol=exchange_symbol, exchange=exchange)
        else:
            raise ProductTableError("You must specify either product_symbol or exchange_symbol")

    def get_exchange_type(self, exchange, product_symbol=None, exchange_symbol=None):
        if product_symbol is not None:
            return self.get("exchange_type", product_symbol=product_symbol, exchange=exchange)
        elif exchange_symbol is not None:
            return self.get("exchange_type", exchange_symbol=exchange_symbol, exchange=exchange)
        else:
            raise ProductTableError("You must specify either product_symbol or exchange_symbol")

    def get_base_currency(self, exchange, product_symbol):
        return self.get("base_currency", product_symbol, exchange)

    def get_quote_currency(self, exchange, product_symbol):
        return self.get("quote_currency", product_symbol, exchange)

    def get_trading_details(self, exchange, product_symbol):
        return {
            "price_precision": self.get("price_precision", product_symbol, exchange),
            "size_precision": self.get("size_precision", product_symbol, exchange),
            "min_size": self.get("min_size", product_symbol, exchange),
            "min_notional": self.get("min_notional", product_symbol, exchange),
            "size_per_contract": self.get("size_per_contract", product_symbol, exchange),
        }

    def get_exchange_symbols(self, exchange, product_type=None, exchange_type=None):
        if product_type is None and exchange_type is None:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .select("exchange_symbol")
                .to_series()
                .to_list()
            )
        elif product_type is not None and exchange_type is None:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .filter(pl.col("product_type") == product_type)
                .select("exchange_symbol")
                .to_series()
                .to_list()
            )
        elif product_type is None and exchange_type is not None:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .filter(pl.col("exchange_type") == exchange_type)
                .select("exchange_symbol")
                .to_series()
                .to_list()
            )
        else:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .filter(pl.col("product_type") == product_type)
                .filter(pl.col("exchange_type") == exchange_type)
                .select("exchange_symbol")
                .to_series()
                .to_list()
            )

    def get_product_symbols(self, exchange, product_type=None, exchange_type=None):
        if product_type is None and exchange_type is None:
            return (
                self.product_table.filter(pl.col("exchange") == exchange).select("product_symbol").to_series().to_list()
            )
        elif product_type is not None and exchange_type is None:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .filter(pl.col("product_type") == product_type)
                .select("product_symbol")
                .to_series()
                .to_list()
            )
        elif product_type is None and exchange_type is not None:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .filter(pl.col("exchange_type") == exchange_type)
                .select("product_symbol")
                .to_series()
                .to_list()
            )
        else:
            return (
                self.product_table.filter(pl.col("exchange") == exchange)
                .filter(pl.col("product_type") == product_type)
                .filter(pl.col("exchange_type") == exchange_type)
                .select("product_symbol")
                .to_series()
                .to_list()
            )
