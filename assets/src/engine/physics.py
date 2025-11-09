from engine.math import Vec2
from engine.entity import Entity

from typing import Iterable


class Physics:
    _accumulator: float  # Used to accumulate how many physics ticks should happen each frame
    fixed_delta_time: float
    gravity: Vec2
    interpolation: bool

    @staticmethod
    def init(fixed_delta_time: float, gravity: Vec2, interpolation: bool):
        Physics._accumulator = 0.0
        Physics.fixed_delta_time = fixed_delta_time
        Physics.gravity = gravity
        Physics.interpolation = interpolation

    @staticmethod
    def _tick(entities: Iterable[Entity], frame_delta_time: float):
        Physics._accumulator += frame_delta_time

        while Physics._accumulator >= Physics.fixed_delta_time:
            for entity in entities:
                if entity.is_ticking() and entity.is_in_play():
                    entity._physics_tick(Physics.fixed_delta_time)

            Physics._accumulator -= Physics.fixed_delta_time

        interpolation_fraction = (Physics._accumulator / Physics.fixed_delta_time) if Physics.interpolation else 1.0
        return interpolation_fraction

    @staticmethod
    def get_fixed_delta_time() -> float:
        return Physics._fixed_delta_time

    @staticmethod
    def set_fixed_delta_time(fixed_delta_time: float):
        Physics._fixed_delta_time = fixed_delta_time

    @staticmethod
    def get_gravity() -> Vec2:
        return Physics._gravity

    @staticmethod
    def set_gravity(gravity: Vec2):
        Physics._gravity = gravity
