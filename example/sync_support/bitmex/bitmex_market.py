import krex


client = krex.bitmex()

try:
    instrument_info = client.get_instrument_info()
    print(instrument_info)
    print("typ：")
    from collections import Counter

    print(Counter([m.get("typ", "") for m in instrument_info]))
    print("IFXXXP：")
    for m in instrument_info:
        if m.get("typ") == "IFXXXP":
            print(m.get("symbol"))
    print("FFWCSX：")
    for m in instrument_info:
        if m.get("typ") == "FFWCSX":
            print(m.get("symbol"))
except Exception as e:
    print(f"Error getting instrument info: {e}")
print("\n" + "=" * 50 + "\n")

orderbook = client.get_orderbook(product_symbol="XBT-USDT-SWAP", depth=10)
print(orderbook)
print("\n" + "=" * 50 + "\n")

trades = client.get_trades(product_symbol="XBT-USDT-SWAP", count=5)
print(trades)
print("\n" + "=" * 50 + "\n")

ticker = client.get_ticker(symbol="XBT-USDT-SWAP", binSize="1m", count=5)
print(ticker)
print("\n" + "=" * 50 + "\n")

kline = client.get_kline(symbol="XBT-USDT-SWAP", binSize="1m", count=5)
print(kline)
print("\n" + "=" * 50 + "\n")

funding = client.get_funding(product_symbol="XBT-USDT-SWAP", count=5)
print(funding)
print("\n" + "=" * 50 + "\n")
