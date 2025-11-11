from engine.entity import Entity
from engine.components import InputComponent, ImageComponent
from engine.math import Vec2
from engine.time import Time
from engine.input import InputEventType
from ninjagame.data import Data


class PlayerEntity(Entity):
    def __init__(self, priority: int = 0):
        super().__init__(priority)
        self._is_ticking = True
        self._speed = 300.0
        self._horizontal_input = 0.0
        self._vertical_input = 0.0

        self._input_component = self.add_component(InputComponent())
        self._image_component = self.add_component(
            ImageComponent(Data.asset_path("data", "images", "clouds", "cloud_1.png")))

    def _enter_play(self):
        super()._enter_play()
        self._input_component.bind_axis("horizontal", self._set_horizontal_input)
        self._input_component.bind_axis("vertical", self._set_vertical_input)
        self._input_component.bind_action("slow_motion", InputEventType.PRESSED, self._toggle_slow_motion)

    def _exit_play(self):
        super()._exit_play()
        self._input_component.unbind_axis("horizontal", self._set_horizontal_input)
        self._input_component.unbind_axis("vertical", self._set_vertical_input)
        self._input_component.unbind_action("slow_motion", InputEventType.PRESSED, self._toggle_slow_motion)

    def _physics_tick(self, fixed_delta_time: float):
        super()._physics_tick(fixed_delta_time)
        horizontal_delta = Vec2.right() * self._speed * self._horizontal_input * fixed_delta_time
        vertical_delta = Vec2.up() * self._speed * self._vertical_input * fixed_delta_time
        position_delta = horizontal_delta + vertical_delta
        transform = self.get_transform()
        transform.set_position(transform.get_position() + position_delta)

    def _set_horizontal_input(self, axis_value: float):
        self._horizontal_input = axis_value

    def _set_vertical_input(self, axis_value: float):
        self._vertical_input = axis_value

    def _toggle_slow_motion(self):
        new_time_scale = 1.0 if Time.get_time_scale() < 1.0 else 0.2
        Time.set_time_scale(new_time_scale)
