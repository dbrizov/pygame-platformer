from typing import Any, Callable


EventDelegate = Callable[[Any], None]


class EventHook():
    def __init__(self):
        self._handlers: list[EventDelegate] = list()

    def __add__(self, handler: EventDelegate):
        self._handlers.append(handler)
        return self

    def __sub__(self, handler: EventDelegate):
        self._handlers.remove(handler)
        return self

    def remove_all_handlers(self):
        self._handlers.clear()

    def invoke(self, *args: Any, **kwargs: Any):
        for handler in self._handlers:
            handler(*args, **kwargs)
