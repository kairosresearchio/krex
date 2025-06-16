"""Helper functions for Jupyter Notebook compatibility."""

import asyncio
import sys
from typing import Optional


def is_jupyter_environment() -> bool:
    """
    檢測是否在 Jupyter 環境中運行

    Returns:
        bool: True if running in Jupyter, False otherwise
    """
    try:
        # 檢查是否有 IPython 核心
        from IPython import get_ipython

        ipython = get_ipython()

        if ipython is None:
            return False

        # 檢查是否在 notebook 或 lab 環境中
        if hasattr(ipython, "kernel"):
            return True

        # 檢查 IPython 的類名
        class_name = ipython.__class__.__name__
        if "ZMQ" in class_name or "Terminal" in class_name:
            return True

        return False
    except ImportError:
        return False


def has_running_event_loop() -> bool:
    """
    檢查是否已經有運行中的事件循環

    Returns:
        bool: True if there's a running event loop, False otherwise
    """
    try:
        loop = asyncio.get_running_loop()
        return loop is not None
    except RuntimeError:
        return False


def ensure_nest_asyncio() -> Optional[str]:
    """
    自動偵測 Jupyter 環境並應用 nest_asyncio

    Returns:
        Optional[str]: 返回狀態訊息，如果不需要應用則返回 None
    """
    # 如果不在 Jupyter 環境中，不需要 nest_asyncio
    if not is_jupyter_environment():
        return None

    # 如果沒有運行中的事件循環，也不需要 nest_asyncio
    if not has_running_event_loop():
        return None

    try:
        import nest_asyncio

        # 檢查是否已經應用過
        if hasattr(asyncio, "_nest_patched"):
            return "nest_asyncio already applied"

        # 應用 nest_asyncio
        nest_asyncio.apply()

        return "nest_asyncio applied successfully for Jupyter environment"

    except ImportError:
        warning_msg = (
            "Warning: Running in Jupyter environment with active event loop, "
            "but nest_asyncio is not installed. "
            "Please install it with: pip install nest_asyncio"
        )
        print(warning_msg, file=sys.stderr)
        return warning_msg


def auto_apply_nest_asyncio(verbose: bool = False) -> None:
    """
    自動應用 nest_asyncio（如果需要的話）

    Args:
        verbose (bool): 是否顯示詳細訊息
    """
    result = ensure_nest_asyncio()

    if verbose and result:
        print(f"[krex] {result}")


# 在模組導入時自動檢查並應用
auto_apply_nest_asyncio(verbose=False)
