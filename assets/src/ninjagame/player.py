from engine.entity import Entity
from engine.components import Component
from engine.components import InputComponent
from engine.input import InputEventType

from typing import Iterable


class PlayerEntity(Entity):
    def __init__(self, priority: int = 0, initial_components: Iterable[Component] | None = None):
        super().__init__(priority, initial_components)

    def init(self):
        super().init()

        self._input_component = self.add_component(InputComponent())
        self._input_component.bind_action("left", InputEventType.EVENT_TYPE_PRESSED, lambda: print("left"))
        self._input_component.bind_action("right", InputEventType.EVENT_TYPE_PRESSED, lambda: print("right"))
        self._input_component.bind_action("up", InputEventType.EVENT_TYPE_PRESSED, lambda: print("up"))
        self._input_component.bind_action("down", InputEventType.EVENT_TYPE_PRESSED, lambda: print("down"))
