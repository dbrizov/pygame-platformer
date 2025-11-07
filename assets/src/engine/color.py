import pygame


class Color(pygame.Color):
    @staticmethod
    def none() -> "Color":
        return Color(0, 0, 0, 0)

    @staticmethod
    def black() -> "Color":
        return Color(0, 0, 0)

    @staticmethod
    def white() -> "Color":
        return Color(255, 255, 255)

    @staticmethod
    def gray() -> "Color":
        return Color(128, 128, 128)

    @staticmethod
    def red() -> "Color":
        return Color(255, 0, 0)

    @staticmethod
    def green() -> "Color":
        return Color(0, 255, 0)

    @staticmethod
    def blue() -> "Color":
        return Color(0, 0, 255)

    @staticmethod
    def yellow() -> "Color":
        return Color(255, 255, 0)

    @staticmethod
    def magenta() -> "Color":
        return Color(255, 0, 255)

    @staticmethod
    def cyan() -> "Color":
        return Color(0, 255, 255)

    @staticmethod
    def orange() -> "Color":
        return Color(255, 165, 0)
