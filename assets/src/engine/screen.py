import pygame
from engine.math import Vec2


class Screen:
    _surface: pygame.Surface

    @staticmethod
    def init(width: int, height: int, flags: int = 0, depth: int = 0):
        Screen._surface = pygame.display.set_mode((width, height), flags, depth)

    @staticmethod
    def repaint():
        pygame.display.flip()

    @staticmethod
    def get_surface() -> pygame.Surface:
        return Screen._surface

    @staticmethod
    def get_size() -> Vec2:
        return Vec2(Screen._surface.get_width(), Screen._surface.get_height())

    @staticmethod
    def get_width() -> int:
        return Screen._surface.get_width()

    @staticmethod
    def get_height() -> int:
        return Screen._surface.get_height()

    @staticmethod
    def set_window_title(caption: str):
        pygame.display.set_caption(caption)
