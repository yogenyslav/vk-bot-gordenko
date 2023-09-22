from typing import Type
from .types.event import Event
from .handler import Handler


class Router:
    def __init__(self) -> None:
        self.handlers: list[Handler] = []

    async def handle(self, event: Event):
        for handler in self.handlers:
            ok = await handler.check(event)
            if ok:
                return await handler.handle(event)
        return None

    def __call__(self, text: str | None = None):
        def wrapper(func):
            self.handlers.append(Handler(func, text))
            return func

        return wrapper
