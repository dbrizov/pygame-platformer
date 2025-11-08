from engine.math import Vec2
from engine.entity import Entity

from typing import Iterable


class Physics:
    _accumulator = 0.0  # Used to accumulate how many physics ticks should happen each frame
    fixed_delta_time = 0.0
    gravity = Vec2.zero()
    interpolation = True

    @staticmethod
    def init(fixed_delta_time: float, gravity: Vec2, interpolation: bool):
        Physics.fixed_delta_time = fixed_delta_time
        Physics.gravity = gravity
        Physics.interpolation = interpolation

    @staticmethod
    def _tick(entities: Iterable[Entity], frame_delta_time: float):
        Physics._accumulator += frame_delta_time
        physics_ticked_this_frame = Physics._accumulator >= Physics.fixed_delta_time

        while Physics._accumulator >= Physics.fixed_delta_time:
            for entity in entities:
                if entity.is_ticking() and entity.is_in_play():
                    entity._physics_tick(Physics.fixed_delta_time)

            Physics._accumulator -= Physics.fixed_delta_time

        interpolation_fraction = 1.0
        if Physics.interpolation and not physics_ticked_this_frame:
            interpolation_fraction = Physics._accumulator / Physics.fixed_delta_time

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
