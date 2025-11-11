import pygame
from engine.time import Time
from engine.input import Input
from engine.physics import Physics
from engine.graphics import Display
from engine.config import EngineConfig
from engine.entity import EntitySpawner


class GameLoop:
    @staticmethod
    def init():
        pygame.init()
        EngineConfig.init()
        Display.init(EngineConfig.SCREEN_WIDTH, EngineConfig.SCREEN_HEIGHT)
        Time.init(EngineConfig.TARGET_FPS)
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

            entities = EntitySpawner.get_entities()
            for entity in entities:
                if entity.is_ticking() and entity.is_in_play():
                    entity._tick(scaled_delta_time)

            # Engine._physics_tick()
            interpolation_fraction = Physics._tick(entities, scaled_delta_time)

            # Engine._render_tick()
            for entity in entities:
                if entity.is_ticking() and entity.is_in_play():
                    entity._render_tick(scaled_delta_time)

            Display.render_frame(interpolation_fraction)

        pygame.quit()
