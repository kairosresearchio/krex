def bybit_convert_timeframe(timeframe: str) -> int:
    """
    bybit, ascendex
    """
    if timeframe == "1m":
        return "1"
    elif timeframe == "3m":
        return "3"
    elif timeframe == "5m":
        return "5"
    elif timeframe == "15m":
        return "15"
    elif timeframe == "30m":
        return "30"
    elif timeframe == "1h":
        return "60"
    elif timeframe == "2h":
        return "120"
    elif timeframe == "4h":
        return "240"
    elif timeframe == "6h":
        return "360"
    elif timeframe == "12h":
        return "720"
    elif timeframe == "1d":
        return "D"
    elif timeframe == "1w":
        return "W"
    elif timeframe == "1m":
        return "M"
    else:
        raise ValueError("timeframe not supported")


def bitmart_convert_timeframe(timeframe: str) -> str:
    if timeframe == "1m":
        return 1
    elif timeframe == "5m":
        return 5
    elif timeframe == "15m":
        return 15
    elif timeframe == "30m":
        return 30
    elif timeframe == "1h":
        return 60
    elif timeframe == "2h":
        return 120
    elif timeframe == "4h":
        return 240
    elif timeframe == "1d":
        return 1440
    elif timeframe == "1w":
        return 10080
    elif timeframe == "1m":
        return 43200
    else:
        raise ValueError("timeframe not supported")


def kucoin_convert_timeframe(timeframe: str) -> str:
    if timeframe == "1m":
        return "1min"
    elif timeframe == "3m":
        return "3min"
    elif timeframe == "5m":
        return "5min"
    elif timeframe == "15m":
        return "15min"
    elif timeframe == "30m":
        return "30min"
    elif timeframe == "1h":
        return "1hour"
    elif timeframe == "2h":
        return "2hour"
    elif timeframe == "4h":
        return "4hour"
    elif timeframe == "6h":
        return "6hour"
    elif timeframe == "8h":
        return "8hour"
    elif timeframe == "12h":
        return "12hour"
    elif timeframe == "1d":
        return "1day"
    elif timeframe == "1w":
        return "1week"
    elif timeframe == "1m":
        return "1month"
    else:
        raise ValueError("timeframe not supported")
