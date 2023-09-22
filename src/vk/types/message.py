from typing import Any, Optional
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
    reply_markup: Optional["ReplyMarkup"] = Field(None)


class ReplyMarkupButtonAction(BaseModel):
    type: Optional[str] = Field(None)
    # payload: Optional[str] = Field(None)
    # app_id: Optional[int] = Field(None)
    # owner_id: Optional[int] = Field(None)
    # hash: Optional[str] = Field(None)
    label: Optional[str] = Field(None)


class ReplyMarkupButton(BaseModel):
    action: ReplyMarkupButtonAction = Field(...)
    color: Optional[str] = Field(None)


class ReplyMarkup(BaseModel):
    one_time: bool = Field(...)
    buttons: list[list[ReplyMarkupButton]] = Field(...)


class MessageNewEvent(GroupEvent):
    object: MessageNewObject = Field(...)
    from_user: User = Field(...)

    async def answer(
        self, text: str, reply_markup: ReplyMarkup | None = None
    ) -> SendMessage:
        return SendMessage(message_event=self, text=text, reply_markup=reply_markup)
