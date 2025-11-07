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

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("Vec2 is immutable")


Vec2.ZERO = Vec2(0, 0)
Vec2.ONE = Vec2(1, 1)
Vec2.LEFT = Vec2(-1, 0)
Vec2.RIGHT = Vec2(1, 0)
Vec2.UP = Vec2(0, -1)
Vec2.DOWN = Vec2(0, 1)


# class Vector2(tuple[float, float]):
#     ZERO: "Vector2"
#     ONE: "Vector2"
#     LEFT: "Vector2"
#     RIGHT: "Vector2"
#     UP: "Vector2"
#     DOWN: "Vector2"

#     def __new__(cls, x: float, y: float):
#         return tuple.__new__(cls, (x, y))

#     @property
#     def x(self):
#         return self[0]

#     @property
#     def y(self):
#         return self[1]

#     def __add__(self, other: "Vector2") -> "Vector2":  # type: ignore[override]
#         return Vector2(self.x + other.x, self.y + other.y)

#     def __sub__(self, other: "Vector2") -> "Vector2":  # type: ignore[override]
#         return Vector2(self.x - other.x, self.y - other.y)

#     def __mul__(self, scalar: float) -> "Vector2":  # type: ignore[override]
#         return Vector2(self.x * scalar, self.y * scalar)

#     def __truediv__(self, scalar: float) -> "Vector2":  # type: ignore[override]
#         return Vector2(self.x / scalar, self.y / scalar)

#     def __eq__(self, other: "Vector2") -> bool:  # type: ignore[override]
#         return self.x == other.x and self.y == other.y

#     def __str__(self):
#         return f"({self.x:.2f}, {self.y:.2f})"

#     def __repr__(self):
#         return f"Vector2({self.x:.2f}, {self.y:.2f})"

#     @property
#     def magnitude(self) -> float:
#         return math.sqrt(self.x * self.x + self.y * self.y)

#     @property
#     def magnitude_sqr(self) -> float:
#         return self.x * self.x + self.y * self.y

#     @property
#     def normalized(self) -> "Vector2":
#         magnitude = self.magnitude
#         if magnitude < Math.EPSILON:
#             return Vector2.ZERO
#         return Vector2(self.x / magnitude, self.y / magnitude)

#     @staticmethod
#     def dot(a: "Vector2", b: "Vector2") -> float:
#         return a.x * b.x + a.y * b.y


# Vector2.ZERO = Vector2(0, 0)
# Vector2.ONE = Vector2(1, 1)
# Vector2.LEFT = Vector2(-1, 0)
# Vector2.RIGHT = Vector2(1, 0)
# Vector2.UP = Vector2(0, -1)
# Vector2.DOWN = Vector2(0, 1)
