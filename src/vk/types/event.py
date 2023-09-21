from enum import Enum
from pydantic import BaseModel, Field


class GroupEventType(str, Enum):
    message_new = "message_new"
    message_reply = "message_reply"
    message_edit = "message_edit"
    message_allow = "message_allow"
    message_deny = "message_deny"
    message_typing_state = "message_typing_state"


class Event(BaseModel):
    type: str = Field(...)


class GroupEvent(Event):
    group_id: int = Field(...)
    event_id: str = Field(...)
    v: str = Field(...)
