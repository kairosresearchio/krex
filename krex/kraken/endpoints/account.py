from enum import Enum



class Account(str, Enum):

    def __str__(self) -> str:
        return self.value
