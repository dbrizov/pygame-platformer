import pygame


class Time:
    _clock = pygame.time.Clock()
    _fps = 60
    _play_time = 0.0

    @staticmethod
    def _tick():
        milliseconds = Time._clock.tick(Time._fps)
        Time._play_time += milliseconds / 1000.0

    @staticmethod
    def get_fps() -> float:
        return Time._clock.get_fps()

    @staticmethod
    def set_fps(fps: int):
        Time._fps = fps

    @staticmethod
    def get_delta_time() -> float:
        milliseconds = Time._clock.get_time()
        return milliseconds / 1000.0

    @staticmethod
    def get_play_time() -> float:
        return Time._play_time
