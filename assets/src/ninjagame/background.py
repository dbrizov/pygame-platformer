import pygame
from engine.entity import Entity
from engine.graphics import Display, RenderStruct
from engine.color import Color


class BackgroundEntity(Entity):
    def __init__(self, priority: int = 0):
        super().__init__(priority)
        self._is_ticking = True
        self._surface = pygame.Surface(Display.get_size())
        self._surface.fill(Color(14, 219, 248))

    def _render_tick(self, delta_time: float):
        super()._render_tick(delta_time)
        transform = self.get_transform()
        render_struct = RenderStruct(self._surface, transform.get_position(), transform.get_prev_position())
        Display.deferred_blit(render_struct)
