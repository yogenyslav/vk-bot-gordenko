from typing import Optional
from pydantic import BaseModel, Field
from .user import User


class Event(BaseModel):
    from_user: Optional[User] = Field(
        None, description="пользователь, отправивший сообщение."
    )
    # type:
