from enum import Enum



class Earn(str, Enum):

    def __str__(self) -> str:
        return self.value
