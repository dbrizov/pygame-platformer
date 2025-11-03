import pygame.display
from pygame import Surface
from engine.vector import Vector2


class Screen:
    _surface: Surface

    @staticmethod
    def init(width: int, height: int, flags=0, depth=0):
        Screen._surface = pygame.display.set_mode((width, height), flags, depth)

    @staticmethod
    def repaint():
        pygame.display.flip()

    @staticmethod
    def get_surface():
        return Screen._surface

    @staticmethod
    def get_size():
        return Vector2(Screen._surface.get_width(), Screen._surface.get_height())

    @staticmethod
    def get_width():
        return Screen._surface.get_width()

    @staticmethod
    def get_height():
        return Screen._surface.get_height()

    @staticmethod
    def set_window_title(caption: str):
        pygame.display.set_caption(caption)
