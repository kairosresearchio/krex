# KREX - A Lightweight Python Package for Low-Latency and Cross-Exchange Trading

A high-performance and lightweight Python library for interacting with cryptocurrency exchanges. KREX offers full synchronous and asynchronous support across major exchanges, designed for speed, modularity, and ease of use.

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/krex.svg)](https://badge.fury.io/py/krex)

## 📦 Installation

```bash
pip install krex
```

## 🚀 Quick Start

### Synchronous Usage

```python
import krex
import os

# Initialize client for any supported exchange
client = krex.binance(
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Get account balance
balance = client.get_account_balance()
print(balance)

# Get market data
klines = client.get_klines(symbol="BTCUSDT", interval="1h")
print(klines)
```

### Asynchronous Usage

```python
import asyncio
import krex.async_support as krex
import os

async def main():
    # Initialize async client
    client = await krex.binance(
        api_key="your_api_key",
        api_secret="your_api_secret"
    )

    try:
        # Get account balance
        balance = await client.get_account_balance()
        print(balance)

        # Get market data
        klines = await client.get_klines(symbol="BTCUSDT", interval="1h")
        print(klines)

    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## 📚 Supported Exchanges

| Exchange | Sync Support | Async Support |
|----------|-------------|---------------|
| **Binance** | ✅ | ✅ |
| **Bybit** | ✅ | ✅ |
| **OKX** | ✅ | ✅ |
| **BitMart** | ✅ | ✅ |
| **Gate.io** | ✅ | ✅ |
| **Hyperliquid** | ✅ | ✅ |
| **BitMEX** | ✅ | ✅ |
| **BingX** | Developing | Developing |
| **AscendEX** | Developing | Developing |
| **KuCoin** | Developing  | Developing  |

## 🔍 Key Features

- 📘 Product Table Manager for unifying trading instruments in different exchanges
- 🔁 Sync & Async API clients with identical interfaces
- ⚡ Optimized for low-latency, high-frequency trading

## What is Product Table Manager(ptm)?

Ptm is a utility that standardizes and unifies trading instrument metadata across different exchanges, making cross-exchange strategy development easier.

It is a table that contains the following columns:

| Column | Description |
|--------|-------------|
| exchange | The exchange name |
| product_symbol | The symbol we use to identify the product, it will be the same in different exchanges. For example, `BTC-USDT-SWAP` is the same product in Binance and Bybit, which named `BTCUSDT` in Binance and `BTC-USDT-SWAP` in OKX. |
| exchange_symbol | The symbol that the exchange will actually used |
| product_type | The type we will use, e.g. `spot`, `inverse`, `swap`, `futures` |
| exchange_type | The type the exchange will actually used, e.g. `linear`, `INVERSE`, `perp`... different exchanges have different types, pretty annoying...|
| base_symbol | The base symbol, e.g. `BTC` |
| quote_symbol | The quote symbol, e.g. `USDT` |
| price_precision | The price precision, e.g. `0.000001` |
| size_precision | The size precision, e.g. `0.000001` |
| min_size | The minimum size, e.g. `0.000001` |
| min_notional | The minimum notional, e.g. `0.000001` |
| multiplier | The multiplier of the product, such symbol like `1000BONKUSDT` in Bybit will need to be multiplied by 1000 to get the actual size, if you are trading across spot and swap, you will need this|
| size_per_contract | The size per contract. Sometimes 1 contract is not the same as 1 unit in exchanges like OKX. |

## How to use Product Table Manager?
In most cases, we have handled the case, but if you have any specific use cases, you can use the `ptm` to get the information you want.

```python

import krex

binance = krex.binance()

btcusdt_product_symbol = binance.ptm.get_product_symbol(
    exchange="binance",
    exchange_symbol="BTCUSDT",
    product_type="swap",
)

print(btcusdt_product_symbol)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](.github/CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kairosresearchio/krex.git
cd krex

# We use `uv` to manage the project, you can install it with `pip install uv`
# Create a virtual environment
uv venv

# Install the dependencies
uv sync
```

### Contributors

<a href="https://github.com/kairosresearchio/krex/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=kairosresearchio/krex" />
</a>

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🆘 Support

- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/kairosresearchio/krex/issues)

## 📜 Disclaimer

Cryptocurrency trading involves significant risk. This library is provided as-is without any warranty. Users are responsible for their own trading decisions and risk management.
