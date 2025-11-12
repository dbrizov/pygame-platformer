import pygame
from engine.time import Time
from engine.input import Input
from engine.physics import Physics
from engine.graphics import Display, Graphics
from engine.config import EngineConfig
from engine.entity import EntitySpawner


class GameLoop:
    @staticmethod
    def init():
        pygame.init()
        EngineConfig.init()
        Time.init(EngineConfig.TARGET_FPS)
        Display.init(EngineConfig.SCREEN_WIDTH, EngineConfig.SCREEN_HEIGHT)
        Graphics.init(EngineConfig.GRAPHICS_SCALE)
        Physics.init(EngineConfig.PHYSICS_DELTA_TIME, EngineConfig.PHYSICS_INTERPOLATION)

    @staticmethod
    def run():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Time._tick()

            EntitySpawner._resolve_entity_spawn_requests()
            EntitySpawner._resolve_entity_destroy_requests()

            delta_time = Time.get_delta_time()
            scaled_delta_time = delta_time * Time.get_time_scale()

            # Engine._tick()
            Input._tick(delta_time)

            tickable_entities = EntitySpawner.get_tickable_entities()
            for entity in tickable_entities:
                entity._tick(scaled_delta_time)

            # Engine._physics_tick()
            Physics._tick(tickable_entities, scaled_delta_time)

            # Engine._render_tick()
            entities = EntitySpawner.get_entities()
            for entity in entities:
                entity._render_tick(scaled_delta_time)

            Display.render_frame(Physics.get_interpolation_fraction())

        pygame.quit()
