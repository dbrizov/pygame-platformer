from engine.entity import Entity
from engine.screen import Screen
from engine.color import Color


class BackgroundEntity(Entity):
    def __init__(self, priority: int = 0):
        super().__init__(priority)
        self._is_ticking = True

    def tick(self, delta_time: float):
        super().tick(delta_time)
        Screen.get_surface().fill(Color(14, 219, 248))
