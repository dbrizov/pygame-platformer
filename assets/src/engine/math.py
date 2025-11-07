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
    @staticmethod
    def zero() -> "Vec2":
        return Vec2(0, 0)

    @staticmethod
    def one() -> "Vec2":
        return Vec2(1, 1)

    @staticmethod
    def left() -> "Vec2":
        return Vec2(-1, 0)

    @staticmethod
    def right() -> "Vec2":
        return Vec2(1, 0)

    @staticmethod
    def up() -> "Vec2":
        return Vec2(0, -1)

    @staticmethod
    def down() -> "Vec2":
        return Vec2(0, 1)
