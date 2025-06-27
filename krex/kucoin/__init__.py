from .client import Client


def kucoin(**kwargs):
    """Create a KuCoin client instance."""
    return Client(**kwargs) 