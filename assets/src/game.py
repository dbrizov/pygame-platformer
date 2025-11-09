from engine.gameloop import EngineSettings, GameLoop
from engine.math import Vec2
from engine.entity import EntitySpawner
from ninjagame.player import PlayerEntity
from ninjagame.background import BackgroundEntity


def spawn_entities():
    EntitySpawner.spawn_entity(BackgroundEntity)
    EntitySpawner.spawn_entity(PlayerEntity)


def run():
    engine_settings = EngineSettings()
    engine_settings.screen_width = 640  # In pixels
    engine_settings.screen_height = 480  # In pixels
    engine_settings.fps = 60
    engine_settings.physics_delta_time = 1.0 / 60.0
    engine_settings.physics_gravity = Vec2.down() * 500
    engine_settings.physics_interpolation = True

    GameLoop.init(engine_settings)

    spawn_entities()

    GameLoop.run()


if __name__ == "__main__":
    run()
