from sortedcontainers import SortedList, SortedSet
from engine.components import Component, TransformComponent

from typing import Any, Type, TypeVar, Iterable


TEntity = TypeVar("TEntity", bound="Entity")
TComponent = TypeVar("TComponent", bound="Component")


class Entity:
    def __init__(self, priority: int = 0):
        """Represents an `Entity` in the game.

        `priority` -> the `priority` indicated in which order the entities will be updated.
        If entity `A` has `priority=0`, and entity `B` has `priority=1`, `A` will be updated before `B`.
        **NOTE: It cannot be changed at runtime**
        """
        self._is_ticking = False
        self._is_in_play = False
        self._priority = priority
        self._transform = TransformComponent()
        self._components = SortedList(iterable=[self._transform], key=(lambda comp: comp._priority))

    def enter_play(self):
        self._is_in_play = True
        for comp in self._components:
            comp.enter_play()

    def exit_play(self):
        self._is_in_play = False
        for comp in self._components:
            comp.exit_play()

    def tick(self, delta_time: float):
        for comp in self._components:
            comp.tick(delta_time)

    def is_ticking(self) -> bool:
        return self._is_ticking

    def is_in_play(self) -> bool:
        return self._is_in_play

    def get_transform(self) -> TransformComponent:
        return self._transform

    def add_component(self, component: TComponent) -> TComponent:
        self._components.add(component)
        component.set_entity(self)
        if self.is_in_play():
            component.enter_play()
        return component

    def remove_component(self, component: Component):
        self._components.remove(component)
        component.set_entity(None)
        if self.is_in_play():
            component.exit_play()

    def get_component(self, component_class: Type[TComponent]):
        for comp in self._components:
            if isinstance(comp, component_class):
                return comp
        return None


class EntitySpawner:
    _entities = SortedSet(key=(lambda entity: entity._priority))
    _entity_spawn_requests = SortedList(key=(lambda entity: entity._priority))
    _entity_destroy_requests = SortedList(key=(lambda entity: entity._priority))

    @staticmethod
    def get_entities() -> Iterable[Entity]:
        """Get all active entities"""
        return EntitySpawner._entities

    @staticmethod
    def spawn_entity(entity_class: Type[TEntity], priority: int = 0, *args: Any) -> Entity:
        """`entity.enter_play()` will be called on the next frame"""
        entity = entity_class(priority, *args)
        EntitySpawner._entity_spawn_requests.add(entity)
        return entity

    @staticmethod
    def destroy_entity(entity: Entity):
        """`entity.exit_play()` will be called on the next frame"""
        EntitySpawner._entity_destroy_requests.add(entity)

    @staticmethod
    def _resolve_entity_spawn_requests():
        for entity in EntitySpawner._entity_spawn_requests:
            EntitySpawner._entities.add(entity)
            entity.enter_play()

        EntitySpawner._entity_spawn_requests.clear()

    @staticmethod
    def _resolve_entity_destroy_requests():
        for entity in EntitySpawner._entity_destroy_requests:
            EntitySpawner._entities.remove(entity)
            entity.exit_play()

        EntitySpawner._entity_destroy_requests.clear()
