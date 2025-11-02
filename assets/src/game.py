import sys
import pygame
from engine.screen import Screen
from engine.time import Time
from engine.input import Input
from engine.input import InputEvent
from engine.entity import Entity
from engine.entity import EntitySpawner
from engine.components import InputComponent


SCREEN_WIDTH = 640  # in pixels
SCREEN_HEIGHT = 480  # in pixels
FPS = 60


class PlayerEntity(Entity):
    def __init__(self, priority=0, initial_components=None):
        super().__init__(priority, initial_components)

    def init(self):
        super().init()

        self._input_component: InputComponent = self.add_component(InputComponent())
        self._input_component.bind_action("left", InputEvent.EVENT_TYPE_PRESSED, lambda: print("left"))
        self._input_component.bind_action("right", InputEvent.EVENT_TYPE_PRESSED, lambda: print("right"))
        self._input_component.bind_action("up", InputEvent.EVENT_TYPE_PRESSED, lambda: print("up"))
        self._input_component.bind_action("down", InputEvent.EVENT_TYPE_PRESSED, lambda: print("down"))


class Game:
    def __init__(self):
        pygame.init()

        Screen.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        Screen.set_window_title("Ninja game")

        Time.set_fps(FPS)

        EntitySpawner.spawn_entity(PlayerEntity)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Time._tick()

            EntitySpawner._resolve_entity_spawn_requests()
            EntitySpawner._resolve_entity_destroy_requests()

            Input._tick(Time.get_delta_time())

            Screen.repaint()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
