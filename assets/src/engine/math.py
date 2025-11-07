import numbers
import pygame

from typing import Any, TypeVar


TNumeric = TypeVar("TNumeric", bound=numbers.Real)


class Math:
    EPSILON = 1e-5

    @staticmethod
    def clamp(value: TNumeric, min: TNumeric, max: TNumeric):
        if (value < min):
            value = min
        elif (value > max):
            value = max
        return value


class Vec2(pygame.math.Vector2):
    ZERO: "Vec2"
    ONE: "Vec2"
    LEFT: "Vec2"
    RIGHT: "Vec2"
    UP: "Vec2"
    DOWN: "Vec2"

    # make it immutable
    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("Vec2 is immutable")


Vec2.ZERO = Vec2(0, 0)
Vec2.ONE = Vec2(1, 1)
Vec2.LEFT = Vec2(-1, 0)
Vec2.RIGHT = Vec2(1, 0)
Vec2.UP = Vec2(0, -1)
Vec2.DOWN = Vec2(0, 1)
