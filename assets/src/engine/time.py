from pygame import time


class Time:
    _clock = time.Clock()
    _fps = 60
    _play_time = 0.0
    _time_scale = 1.0

    @staticmethod
    def tick():
        milliseconds = Time._clock.tick(Time._fps)
        Time._play_time += milliseconds / 1000.0

    @staticmethod
    def get_fps():
        return Time._clock.get_fps()

    @staticmethod
    def set_fps(fps: int):
        Time._fps = fps

    @staticmethod
    def get_delta_time():
        milliseconds = Time._clock.get_time()
        return milliseconds / 1000.0

    @staticmethod
    def get_play_time():
        return Time._play_time

    @staticmethod
    def get_time_scale():
        return Time._time_scale

    @staticmethod
    def set_time_scale(time_scale: float):
        if (time_scale < 0.0):
            time_scale = 0.0

        Time._time_scale = time_scale
