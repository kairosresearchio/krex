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
