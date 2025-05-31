from enum import Enum


class Asset(str, Enum):
    USERVAULTEQUITIES = "userVaultEquities"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return repr(self.value)
