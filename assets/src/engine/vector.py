import math


class Vector2(tuple[float, float, float, float]):
    ZERO: "Vector2"

    def __new__(cls, x: float, y: float):
        return tuple.__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2":
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> "Vector2":
        return Vector2(self.x / scalar, self.y / scalar)

    def __eq__(self, other: "Vector2") -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "({0:.2f}, {1:.2f})".format(self.x, self.y)

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def magnitude_sqr(self) -> float:
        return self.x * self.x + self.y * self.y

    @property
    def normalized(self) -> "Vector2":
        return Vector2(self.x / self.magnitude, self.y / self.magnitude)


Vector2.ZERO = Vector2(0, 0)
