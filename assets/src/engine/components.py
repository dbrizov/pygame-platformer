import pygame
from engine.vector import Vector2
from engine.input import Input
from engine.input import InputEvent
from engine.input import InputEventType

from typing import Callable


ActionDelegate = Callable[[], None]
AxisDelegate = Callable[[float], None]


class ComponentPriority:
    INPUT_COMPONENT = -150
    TRANSFORM_COMPONENT = -100
    DEFAULT_COMPONENT = 0
    RENDER_COMPONENT = 100


class Component(object):
    def __init__(self):
        """The components in the `entity_component_list` of an `entity` are sorted by their `priority`.
        **The `priority` cannot be changed at runtime**
        """
        self._priority = ComponentPriority.DEFAULT_COMPONENT

    def init(self):
        pass

    def enter_play(self):
        pass

    def exit_play(self):
        pass

    def tick(self, delta_time: float):
        pass


class TransformComponent(Component):
    def __init__(self):
        super().__init__()
        self._priority = ComponentPriority.TRANSFORM_COMPONENT
        self.position = Vector2.ZERO


class InputComponent(Component):
    def __init__(self):
        super().__init__()
        self._priority = ComponentPriority.INPUT_COMPONENT
        self._bound_functions_by_axis: dict[str, list[AxisDelegate]] = dict()
        self._bound_functions_by_pressed_action: dict[str, list[ActionDelegate]] = dict()
        self._bound_functions_by_released_action: dict[str, list[ActionDelegate]] = dict()

    def enter_play(self):
        super().enter_play()
        Input.on_input_event += self._on_input_event

    def exit_play(self):
        super().exit_play()
        Input.on_input_event -= self._on_input_event

    def bind_axis(self, axis_name: str, function: AxisDelegate):
        if axis_name not in self._bound_functions_by_axis:
            self._bound_functions_by_axis[axis_name] = list()
        self._bound_functions_by_axis[axis_name].append(function)

    def unbind_axis(self, axis_name: str, function: AxisDelegate):
        self._bound_functions_by_axis[axis_name].remove(function)

    def bind_action(self, action_name: str, event_type: InputEventType, function: ActionDelegate):
        if event_type == InputEventType.EVENT_TYPE_PRESSED:
            if action_name not in self._bound_functions_by_pressed_action:
                self._bound_functions_by_pressed_action[action_name] = list()
            self._bound_functions_by_pressed_action[action_name].append(function)
        elif event_type == InputEventType.EVENT_TYPE_RELEASED:
            if action_name not in self._bound_functions_by_released_action:
                self._bound_functions_by_released_action[action_name] = list()
            self._bound_functions_by_released_action[action_name].append(function)

    def unbind_action(self, action_name: str, event_type: InputEventType, function: ActionDelegate):
        if event_type == InputEventType.EVENT_TYPE_PRESSED:
            self._bound_functions_by_pressed_action[action_name].remove(function)
        elif event_type == InputEventType.EVENT_TYPE_RELEASED:
            self._bound_functions_by_released_action[action_name].remove(function)

    def clear_bindings(self):
        self._bound_functions_by_axis.clear()
        self._bound_functions_by_pressed_action.clear()
        self._bound_functions_by_released_action.clear()

    def _on_input_event(self, input_event: InputEvent):
        if input_event.type == InputEventType.EVENT_TYPE_AXIS:
            if input_event.name in self._bound_functions_by_axis:
                for func in self._bound_functions_by_axis[input_event.name]:
                    func(input_event.axis_value)
        elif input_event.type == InputEventType.EVENT_TYPE_PRESSED:
            if input_event.name in self._bound_functions_by_pressed_action:
                for func in self._bound_functions_by_pressed_action[input_event.name]:
                    func()
        elif input_event.type == InputEventType.EVENT_TYPE_RELEASED:
            if input_event.name in self._bound_functions_by_released_action:
                for func in self._bound_functions_by_released_action[input_event.name]:
                    func()


class ImageComponent(Component):
    def __init__(self, path_to_img: str):
        super().__init__()
        pygame.image.load(path_to_img)
