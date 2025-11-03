from engine.components import TransformComponent
from sortedcontainers import SortedList
from sortedcontainers import SortedSet


class Entity:
    def __init__(self, priority=0, initial_components=None):
        """Represents an entity (game object) in the game

        `priority` -> the `priority` indicated in which order the entities will be updated.
        If entity `A` has `priority=0`, and entity `B` has `priority=1`, `A` will be updated before `B`.
        **It cannot be changed at runtime**

        `initial_components` -> the initial components list
        """
        self.is_ticking = True
        self._is_in_play = False
        self._priority = priority
        self._transform = TransformComponent()
        self._components = SortedList(iterable=[self._transform], key=(lambda comp: comp._priority))
        if initial_components is not None:
            self._components.update(initial_components)

    def init(self):
        for comp in self._components:
            comp.init(self)

    def enter_play(self):
        self._is_in_play = True
        for comp in self._components:
            comp.enter_play()

    def exit_play(self):
        self._is_in_play = False
        for comp in self._components:
            comp.exit_play()

    def tick(self, delta_time: float):
        if self.is_ticking:
            for comp in self._components:
                comp.tick(delta_time)

    def is_in_play(self):
        return self._is_in_play

    def get_transform(self):
        return self._transform

    def add_component(self, component):
        self._components.add(component)
        component.init(self)
        if self.is_in_play():
            component.enter_play()
        return component

    def remove_component(self, component):
        self._components.remove(component)
        if self.is_in_play():
            component.exitPlay()

    def get_component(self, class_obj):
        for comp in self._components:
            if isinstance(comp, class_obj):
                return comp
        return None


class EntitySpawner:
    _entities = SortedSet(key=(lambda entity: entity._priority))
    _entity_spawn_requests = SortedList(key=(lambda entity: entity._priority))
    _entity_destroy_requests = SortedList(key=(lambda entity: entity._priority))

    @staticmethod
    def get_entities():
        """Get all active entities"""
        return EntitySpawner._entities

    @staticmethod
    def spawn_entity(entity_class, *args, priority=0, initial_components=None) -> Entity:
        """`entity.init()` is called immediatelly. `entity.enter_play()` will be called on the next frame"""
        entity = entity_class(*args, priority, initial_components)
        entity.init()
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
