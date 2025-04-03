from enum import Enum



class SubAccount(str, Enum):

    def __str__(self) -> str:
        return self.value
