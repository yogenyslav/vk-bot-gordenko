from typing import Any
from pydantic import BaseModel, Field
from .event import GroupEvent
from .user import User


class ClientInfo(BaseModel):
    button_actions: list[str] = Field(...)
    keyboard: bool = Field(...)
    inline_keyboard: bool = Field(...)
    carousel: bool = Field(...)
    lang_id: int = Field(...)


class MessageNew(BaseModel):
    date: int = Field(...)
    from_id: int = Field(...)
    id: int = Field(...)
    out: int = Field(...)
    attachments: list[Any] = Field(...)  # TODO: attachments
    conversation_message_id: int = Field(...)
    fwd_messages: list[Any] = Field(...)  # TODO: fwd_messages
    important: bool = Field(...)
    is_hidden: bool = Field(...)
    peer_id: int = Field(...)
    random_id: int = Field(...)
    text: str = Field(...)


class MessageNewObject(BaseModel):
    message: MessageNew = Field(...)
    client_info: ClientInfo = Field(...)


class SendMessage(BaseModel):
    message_event: "MessageNewEvent" = Field(...)
    text: str = Field(...)


class MessageNewEvent(GroupEvent):
    object: MessageNewObject = Field(...)
    from_user: User = Field(...)

    async def answer(self, text: str) -> SendMessage:
        return SendMessage(message_event=self, text=text)
