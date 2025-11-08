import numbers
import pygame

from typing import TypeVar


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
    _ZERO: "Vec2"
    _ONE: "Vec2"
    _LEFT: "Vec2"
    _RIGHT: "Vec2"
    _UP: "Vec2"
    _DOWN: "Vec2"

    @staticmethod
    def zero() -> "Vec2":
        return Vec2._ZERO.copy()

    @staticmethod
    def one() -> "Vec2":
        return Vec2._ONE.copy()

    @staticmethod
    def left() -> "Vec2":
        return Vec2._LEFT.copy()

    @staticmethod
    def right() -> "Vec2":
        return Vec2._RIGHT.copy()

    @staticmethod
    def up() -> "Vec2":
        return Vec2._UP.copy()

    @staticmethod
    def down() -> "Vec2":
        return Vec2._DOWN.copy()


Vec2._ZERO = Vec2(0, 0)
Vec2._ONE = Vec2(1, 1)
Vec2._LEFT = Vec2(-1, 0)
Vec2._RIGHT = Vec2(1, 0)
Vec2._UP = Vec2(0, -1)
Vec2._DOWN = Vec2(0, 1)
