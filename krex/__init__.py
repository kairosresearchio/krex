"""
KREX - Kairos Research Exchange Library

A comprehensive library for cryptocurrency exchange interactions with both sync and async support.
Automatically handles Jupyter Notebook compatibility with nest_asyncio.
"""

# 自動處理 Jupyter 環境的 nest_asyncio
from .utils.jupyter_helper import auto_apply_nest_asyncio

VERSION = "0.0.0"

# 在導入時自動應用（如果需要的話）
auto_apply_nest_asyncio(verbose=False)

__version__ = VERSION
__all__ = ["VERSION", "__version__"]
