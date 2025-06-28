"""Helper functions for Jupyter Notebook compatibility."""

import asyncio
import sys
from typing import Optional


def is_jupyter_environment() -> bool:
    """
    Check if the code is running in a Jupyter Notebook or JupyterLab environment.

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
    Check if there's a running asyncio event loop.

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
    Ensure that nest_asyncio is applied if running in a Jupyter environment with an active event loop.

    Returns:
        Optional[str]: A message indicating the result of the operation, or None if no action is needed.
    """
    # If not in Jupyter environment, no need to apply nest_asyncio
    if not is_jupyter_environment():
        return None

    # If there's no running event loop, no need to apply nest_asyncio
    if not has_running_event_loop():
        return None

    try:
        import nest_asyncio

        # Check if nest_asyncio is already applied
        if hasattr(asyncio, "_nest_patched"):
            return "nest_asyncio already applied"

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
    Automatically check and apply nest_asyncio if running in a Jupyter environment with an active event loop.

    Args:
        verbose (bool): If True, prints the result of the operation.
    """
    result = ensure_nest_asyncio()

    if verbose and result:
        print(f"[krex] {result}")


# Automatically apply nest_asyncio if in Jupyter environment with active event loop
auto_apply_nest_asyncio(verbose=False)
