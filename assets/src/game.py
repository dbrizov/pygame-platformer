from engine.gameloop import GameLoop
from engine.graphics import Display
from engine.entity import EntitySpawner
from ninjagame.player import PlayerEntity
from ninjagame.background import BackgroundEntity


def init_game():
    Display.set_window_title("Ninja Game")

    EntitySpawner.spawn_entity(BackgroundEntity)
    EntitySpawner.spawn_entity(PlayerEntity)


def run():
    GameLoop.init()

    init_game()

    GameLoop.run()


if __name__ == "__main__":
    run()
