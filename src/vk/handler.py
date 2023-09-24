from typing import Callable
from .types.event import Event
from .types.message import MessageNewEvent


class Handler:
    def __init__(
        self,
        func: Callable,
        text: str | list[str] | None = None,
        starts_with: str | None = None,
    ):
        self.func = func
        self.text = text
        self.starts_with = starts_with
        if text is None and starts_with is None:
            raise ValueError("no filters were specified")

    async def check(self, event: Event):
        if isinstance(event, MessageNewEvent):
            if isinstance(self.text, list):
                if event.object.message.text in self.text:
                    return True
            elif event.object.message.text == self.text:
                return True
            elif self.starts_with:
                if event.object.message.text.startswith(self.starts_with):
                    return True
            elif self.text == "test_answer":
                return True

        return False

    async def handle(self, event: Event):
        return await self.func(event)
