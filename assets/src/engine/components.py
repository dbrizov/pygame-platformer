import pygame
from pathlib import Path
from engine.vector import Vector2
from engine.color import Color
from engine.input import Input
from engine.input import InputEvent
from engine.input import InputEventType
from engine.screen import Screen

from typing import Callable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.entity import Entity


ActionDelegate = Callable[[], None]
AxisDelegate = Callable[[float], None]


class ComponentPriority:
    INPUT_COMPONENT = -150
    TRANSFORM_COMPONENT = -100
    DEFAULT_COMPONENT = 0
    RENDER_COMPONENT = 100


class Component(object):
    def __init__(self, priority: int = ComponentPriority.DEFAULT_COMPONENT):
        """The base component class for all components.

        Params:
            priority (int): The components attached to an `entity` are sorted by their `priority`. **NOTE: It cannot be changed at runtime**
        """
        self._priority = priority
        self._entity: "Entity | None" = None

    def enter_play(self):
        pass

    def exit_play(self):
        pass

    def tick(self, delta_time: float):
        pass

    def set_entity(self, entity: "Entity | None"):
        self._entity = entity

    def get_entity(self) -> "Entity | None":
        return self._entity


class TransformComponent(Component):
    def __init__(self, priority: int = ComponentPriority.TRANSFORM_COMPONENT):
        """A `Transform Component` stores an `Entity`'s position. An `Entity` always has a `Transform Component`."""
        super().__init__(priority)
        self.position = Vector2.ZERO


class InputComponent(Component):
    def __init__(self, priority: int = ComponentPriority.INPUT_COMPONENT):
        """An `Input Component` enables an `Entity` to bind various forms of input events to delegate functions."""
        super().__init__(priority)
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
    def __init__(self, img_path: str | Path, color_key: Color = Color.BLACK, priority: int = ComponentPriority.RENDER_COMPONENT):
        """An `Image Component` renders an image on the screen.

        Params:
            img_path (str): The path to the image asset so it can be loaded
            color_key (Color): Transparent color key. All pixels matching this key will be transparent
        """
        super().__init__(priority)
        self._image = pygame.image.load(img_path)
        self._image.set_colorkey(color_key)

    def tick(self, delta_time: float):
        super().tick(delta_time)
        entity = self.get_entity()
        if entity is not None:
            transform = entity.get_transform()
            Screen.get_surface().blit(self._image, transform.position)
