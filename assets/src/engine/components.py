import pathlib
import pygame
from engine.math import Vec2
from engine.color import Color
from engine.input import Input, InputEvent, InputEventType
from engine.graphics import Display, RenderStruct

from typing import Callable, TYPE_CHECKING
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

    def _enter_play(self):
        pass

    def _exit_play(self):
        pass

    def _tick(self, delta_time: float):
        pass

    def _physics_tick(self, delta_time: float):
        pass

    def _render_tick(self, delta_time: float):
        pass

    def _set_entity(self, entity: "Entity | None"):
        self._entity = entity

    def get_entity(self) -> "Entity | None":
        return self._entity

    def get_entity_transform(self) -> "TransformComponent":
        entity = self.get_entity()
        assert entity is not None
        return entity.get_transform()


class TransformComponent(Component):
    def __init__(self, priority: int = ComponentPriority.TRANSFORM_COMPONENT):
        """A `Transform Component` stores an `Entity`'s position. An `Entity` always has a `Transform Component`."""
        super().__init__(priority)
        self._position = Vec2.zero()
        self._prev_position = Vec2.zero()

    def get_prev_position(self) -> Vec2:
        return self._prev_position

    def get_position(self) -> Vec2:
        return self._position

    def set_position(self, position: Vec2):
        self._prev_position = self._position
        self._position = position


class RigidBodyComponent(Component):
    def __init__(self, priority: int = ComponentPriority.DEFAULT_COMPONENT):
        """A `RigidBody Component` controls an `Entity`'s position through physics simulation."""
        super().__init__(priority)


class ImageComponent(Component):
    def __init__(self, img_path: str | pathlib.Path, color_key: Color = Color.black(), priority: int = ComponentPriority.RENDER_COMPONENT):
        """An `Image Component` renders an image on the screen.

        Params:
            img_path (str): The path to the image asset so it can be loaded
            color_key (Color): Transparent color key. All pixels matching this key will be transparent
        """
        super().__init__(priority)
        self._image = pygame.image.load(img_path)
        self._image.set_colorkey(color_key)

    def _render_tick(self, delta_time: float):
        super()._render_tick(delta_time)
        transform = self.get_entity_transform()
        render_struct = RenderStruct(self._image, transform.get_position(), transform.get_prev_position())
        Display.deferred_blit(render_struct)


class InputComponent(Component):
    def __init__(self, priority: int = ComponentPriority.INPUT_COMPONENT):
        """An `Input Component` enables an `Entity` to bind various forms of input events to delegate functions."""
        super().__init__(priority)
        self._bound_functions_by_axis: dict[str, list[AxisDelegate]] = dict()
        self._bound_functions_by_pressed_action: dict[str, list[ActionDelegate]] = dict()
        self._bound_functions_by_released_action: dict[str, list[ActionDelegate]] = dict()

    def _enter_play(self):
        super()._enter_play()
        Input.on_input_event += self._on_input_event

    def _exit_play(self):
        super()._exit_play()
        Input.on_input_event -= self._on_input_event

    def _on_input_event(self, input_event: InputEvent):
        if input_event.type == InputEventType.AXIS:
            if input_event.name in self._bound_functions_by_axis:
                for func in self._bound_functions_by_axis[input_event.name]:
                    func(input_event.axis_value)
        elif input_event.type == InputEventType.PRESSED:
            if input_event.name in self._bound_functions_by_pressed_action:
                for func in self._bound_functions_by_pressed_action[input_event.name]:
                    func()
        elif input_event.type == InputEventType.RELEASED:
            if input_event.name in self._bound_functions_by_released_action:
                for func in self._bound_functions_by_released_action[input_event.name]:
                    func()

    def bind_axis(self, axis_name: str, function: AxisDelegate):
        if axis_name not in self._bound_functions_by_axis:
            self._bound_functions_by_axis[axis_name] = list()
        self._bound_functions_by_axis[axis_name].append(function)

    def unbind_axis(self, axis_name: str, function: AxisDelegate):
        self._bound_functions_by_axis[axis_name].remove(function)

    def bind_action(self, action_name: str, event_type: InputEventType, function: ActionDelegate):
        if event_type == InputEventType.PRESSED:
            if action_name not in self._bound_functions_by_pressed_action:
                self._bound_functions_by_pressed_action[action_name] = list()
            self._bound_functions_by_pressed_action[action_name].append(function)
        elif event_type == InputEventType.RELEASED:
            if action_name not in self._bound_functions_by_released_action:
                self._bound_functions_by_released_action[action_name] = list()
            self._bound_functions_by_released_action[action_name].append(function)

    def unbind_action(self, action_name: str, event_type: InputEventType, function: ActionDelegate):
        if event_type == InputEventType.PRESSED:
            self._bound_functions_by_pressed_action[action_name].remove(function)
        elif event_type == InputEventType.RELEASED:
            self._bound_functions_by_released_action[action_name].remove(function)

    def clear_bindings(self):
        self._bound_functions_by_axis.clear()
        self._bound_functions_by_pressed_action.clear()
        self._bound_functions_by_released_action.clear()
