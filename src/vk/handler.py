from typing import Callable
from .types.event import Event
from .types.message import MessageNewEvent


class Handler:
    def __init__(self, func: Callable, text: str | list[str] | None):
        self.func = func
        self.text = text

    async def check(self, event: Event):
        if isinstance(event, MessageNewEvent):
            if isinstance(self.text, list):
                if event.object.message.text in self.text:
                    return True
            elif event.object.message.text == self.text:
                return True
            else:
                return True

        return False

    async def handle(self, event: Event):
        return await self.func(event)
