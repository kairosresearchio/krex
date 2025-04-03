from enum import Enum



class OTC(str, Enum):

    def __str__(self) -> str:
        return self.value
