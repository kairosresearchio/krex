from enum import Enum


class Market(str, Enum):
    META = "meta"
    SPOTMETA = "spotMeta"
    METAANDASSETCTXS = "metaAndAssetCtxs"
    SPOTMETAANDASSETCTXS = "spotMetaAndAssetCtxs"
    L2BOOK = "l2Book"
    CANDLESNAPSHOT = "candleSnapshot"
    FUNDINGHISTORY = "fundingHistory"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return repr(self.value)
