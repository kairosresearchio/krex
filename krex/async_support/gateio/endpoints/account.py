from enum import Enum


class FutureAccount(str, Enum):
    QUERY_FUTURES_ACCOUNT = "/futures/{settle}/accounts"
    QUERY_ACCOUNT_BOOK = "/futures/{settle}/account_book"

    def __str__(self) -> str:
        return self.value


class DeliveryAccount(str, Enum):
    QUERY_DELIVERY_ACCOUNT = "/delivery/{settle}/accounts"
    QUERY_ACCOUNT_BOOK = "/delivery/{settle}/account_book"

    def __str__(self) -> str:
        return self.value


class SpotAccount(str, Enum):
    QUERY_SPOT_ACCOUNT = "/spot/accounts"
    QUERY_ACCOUNT_BOOK = "/spot/account_book"

    def __str__(self) -> str:
        return self.value
