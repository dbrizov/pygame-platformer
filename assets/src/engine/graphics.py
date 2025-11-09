import pygame
from engine.math import Vec2


class RenderStruct:
    def __init__(self, surface: pygame.Surface, position: Vec2, prev_position: Vec2):
        self.surface = surface
        self.position = position
        self.prev_position = prev_position


class Display:
    _surface: pygame.Surface
    _render_queue: list[RenderStruct]

    @staticmethod
    def init(width: int, height: int, flags: int = 0, depth: int = 0):
        Display._surface = pygame.display.set_mode((width, height), flags, depth)
        Display._render_queue = list()

    @staticmethod
    def deferred_blit(render_struct: RenderStruct):
        Display._render_queue.append(render_struct)

    @staticmethod
    def render_frame(interpolation_fraction: float):
        for struct in Display._render_queue:
            position = struct.prev_position.lerp(struct.position, interpolation_fraction)
            Display._surface.blit(struct.surface, position)
        Display._render_queue.clear()
        pygame.display.flip()

    @staticmethod
    def get_size() -> Vec2:
        return Vec2(*Display._surface.get_size())

    @staticmethod
    def get_width() -> int:
        return Display._surface.get_width()

    @staticmethod
    def get_height() -> int:
        return Display._surface.get_height()

    @staticmethod
    def set_window_title(caption: str):
        pygame.display.set_caption(caption)
