from typing import Callable
from .types.event import Event
from .types.message import MessageNewEvent


class Handler:
    def __init__(self, func: Callable, text: str):
        self.func = func
        self.text = text

    async def check(self, event: Event):
        if isinstance(event, MessageNewEvent):
            if event.object.message.text == self.text:
                return True
        return False

    async def handle(self, event: Event):
        return await self.func(event)
