import sys
import pygame
from engine.screen import Screen
from engine.time import Time


SCREEN_WIDTH = 640  # in pixels
SCREEN_HEIGHT = 480  # in pixels
FPS = 30


class Game:
    def __init__(self):
        pygame.init()

        Screen.init(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        Screen.set_window_title("Ninja game")

        Time.set_fps(FPS)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Time.tick()
            Screen.repaint()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
