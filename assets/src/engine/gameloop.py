import pygame
from engine.math import Vec2
from engine.time import Time
from engine.input import Input
from engine.physics import Physics
from engine.graphics import Display
from engine.entity import EntitySpawner


class EngineSettings:
    def __init__(self):
        self.screen_width: int
        self.screen_height: int
        self.fps: int
        self.physics_delta_time: float
        self.physics_gravity: Vec2
        self.physics_interpolation = True


class GameLoop:
    @staticmethod
    def init(settings: EngineSettings):
        pygame.init()
        Display.init(settings.screen_width, settings.screen_height)
        Time.init(settings.fps)
        Physics.init(settings.physics_delta_time, settings.physics_gravity, settings.physics_interpolation)

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
