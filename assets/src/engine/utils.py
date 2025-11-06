from typing import TypeVar


TNumeric = TypeVar("TNumeric", bound=float)  # works for int and float


class Utils:
    @staticmethod
    def clamp(value: TNumeric, min: TNumeric, max: TNumeric):
        if (value < min):
            value = min
        elif (value > max):
            value = max
        return value
