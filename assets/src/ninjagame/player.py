from engine.entity import Entity
from engine.components import InputComponent, ImageComponent
from engine.math import Vec2
from ninjagame.data import Data


class PlayerEntity(Entity):
    def __init__(self, priority: int = 0):
        super().__init__(priority)
        self._is_ticking = True
        self._speed = 600.0
        self._horizontal_input = 0.0
        self._vertical_input = 0.0

        self._input_component = self.add_component(InputComponent())
        self._image_component = self.add_component(
            ImageComponent(Data.asset_path("data", "images", "clouds", "cloud_1.png")))

    def _enter_play(self):
        super()._enter_play()
        self._input_component.bind_axis("horizontal", self._set_horizontal_input)
        self._input_component.bind_axis("vertical", self._set_vertical_input)

    def _exit_play(self):
        super()._exit_play()
        self._input_component.unbind_axis("horizontal", self._set_horizontal_input)
        self._input_component.unbind_axis("vertical", self._set_vertical_input)

    def _physics_tick(self, delta_time: float):
        super()._physics_tick(delta_time)
        horizontal_movement = Vec2.right() * self._speed * self._horizontal_input * delta_time
        vertical_movement = Vec2.up() * self._speed * self._vertical_input * delta_time
        movement = horizontal_movement + vertical_movement
        self.get_transform().position += movement

    def _set_horizontal_input(self, axis_value: float):
        self._horizontal_input = axis_value

    def _set_vertical_input(self, axis_value: float):
        self._vertical_input = axis_value
