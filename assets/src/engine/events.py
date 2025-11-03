class EventHook():
    def __init__(self):
        self._handlers = []

    def __add__(self, handler):
        self._handlers.append(handler)
        return self

    def __sub__(self, handler):
        self._handlers.remove(handler)
        return self

    def remove_all_handlers(self):
        self._handlers.clear()

    def invoke(self, *args, **kwargs):
        for handler in self._handlers:
            handler(*args, **kwargs)
