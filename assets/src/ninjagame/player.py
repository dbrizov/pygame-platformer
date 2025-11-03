from engine.entity import Entity
from engine.components import InputComponent
from engine.input import InputEvent


class PlayerEntity(Entity):
    def __init__(self, priority=0, initial_components=None):
        super().__init__(priority, initial_components)

    def init(self):
        super().init()

        self._input_component: InputComponent = self.add_component(InputComponent())
        self._input_component.bind_action("left", InputEvent.EVENT_TYPE_PRESSED, lambda: print("left"))
        self._input_component.bind_action("right", InputEvent.EVENT_TYPE_PRESSED, lambda: print("right"))
        self._input_component.bind_action("up", InputEvent.EVENT_TYPE_PRESSED, lambda: print("up"))
        self._input_component.bind_action("down", InputEvent.EVENT_TYPE_PRESSED, lambda: print("down"))
        self._input_component.bind_axis("horizontal", lambda axis: print(f"{axis}"))
