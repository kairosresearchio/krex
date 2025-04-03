from enum import Enum



class Funding(str, Enum):

    def __str__(self) -> str:
        return self.value
