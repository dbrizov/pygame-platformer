import pygame
from engine.math import Vec2
from engine.time import Time
from engine.input import Input
from engine.screen import Screen
from engine.physics import Physics
from engine.entity import EntitySpawner
from ninjagame.player import PlayerEntity
from ninjagame.background import BackgroundEntity


SCREEN_WIDTH = 640  # In pixels
SCREEN_HEIGHT = 480  # In pixels
FPS = 60
PHYSICS_DELTA_TIME = 1.0 / 60.0
PHYSICS_GRAVITY = Vec2.down() * 500
PHYSICS_INTERPOLATION = True


class Game:
    def __init__(self):
        pygame.init()

        Screen.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        Screen.set_window_title("Ninja Game")

        Time.set_fps(FPS)

        Physics.init(PHYSICS_DELTA_TIME, PHYSICS_GRAVITY, PHYSICS_INTERPOLATION)

        EntitySpawner.spawn_entity(BackgroundEntity)
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

            # Frame tick
            delta_time = Time.get_delta_time()

            Input._tick(delta_time)

            entities = EntitySpawner.get_entities()
            for entity in entities:
                if entity.is_ticking() and entity.is_in_play():
                    entity._tick(delta_time)

            # Physics tick
            interpolation_fraction = Physics._tick(entities, delta_time)

            # Render
            Screen.render_frame(interpolation_fraction)

        pygame.quit()


if __name__ == "__main__":
    Game().run()
