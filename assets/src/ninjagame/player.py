from engine.entity import Entity
# from engine.input import InputEventType
from engine.components import InputComponent
from engine.components import ImageComponent
from engine.time import Time
from engine.math import Vector2
from ninjagame.data import Data


class PlayerEntity(Entity):
    def __init__(self, priority: int = 0):
        super().__init__(priority)
        self._is_ticking = True
        self._speed = 200

        self._input_component = self.add_component(InputComponent())
        self._image_component = self.add_component(
            ImageComponent(Data.asset_path("data", "images", "clouds", "cloud_1.png")))

    def enter_play(self):
        super().enter_play()
        self._input_component.bind_axis("horizontal", self.move_horizontal)
        self._input_component.bind_axis("vertical", self.move_vertical)

    def exit_play(self):
        super().exit_play()
        self._input_component.unbind_axis("horizontal", self.move_horizontal)
        self._input_component.unbind_axis("vertical", self.move_vertical)

    def move_horizontal(self, axis_value: float):
        transform = self.get_transform()
        new_position = transform.position + Vector2(self._speed * axis_value * Time.get_delta_time(), 0)
        transform.position = new_position

    def move_vertical(self, axis_value: float):
        transform = self.get_transform()
        new_position = transform.position - Vector2(0, self._speed * axis_value * Time.get_delta_time())
        transform.position = new_position
