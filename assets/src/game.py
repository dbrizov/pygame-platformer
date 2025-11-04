import pygame
from engine.screen import Screen
from engine.time import Time
from engine.input import Input
from engine.entity import EntitySpawner
from ninjagame.player import PlayerEntity


SCREEN_WIDTH = 640  # in pixels
SCREEN_HEIGHT = 480  # in pixels
FPS = 60


class Game:
    def __init__(self):
        pygame.init()

        Screen.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        Screen.set_window_title("Ninja Game")

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

            delta_time = Time.get_delta_time()
            time_scale = Time.get_time_scale()

            Input._tick(delta_time)

            for entity in EntitySpawner.get_entities():
                entity.tick(delta_time * time_scale)

            Screen.repaint()

        pygame.quit()


if __name__ == "__main__":
    Game().run()
