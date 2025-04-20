import polars as pl
from typing import Any


def to_dataframe(data: Any, schema: list[str] = None) -> pl.DataFrame:
    if not data:
        return pl.DataFrame()

    if isinstance(data, list):
        if schema:
            return pl.DataFrame(data, schema=schema, orient="row")
        elif all(isinstance(item, dict) for item in data):
            return pl.DataFrame(data)
        else:
            return pl.DataFrame(data, orient="row")

    if isinstance(data, dict):
        return pl.DataFrame([data])

    return pl.DataFrame()
