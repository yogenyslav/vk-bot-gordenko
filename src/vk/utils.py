from pydantic import BaseModel
from .types.message import ReplyMarkup, ReplyMarkupButton, ReplyMarkupButtonAction


class Button(BaseModel):
    text: str


def reply_keyboard(one_time: bool, *args: Button) -> ReplyMarkup:
    return ReplyMarkup(
        one_time=one_time,
        buttons=[
            [
                ReplyMarkupButton(
                    action=ReplyMarkupButtonAction(type="text", label=btn.text),
                    color="primary",
                )
            ]
            for btn in args
        ],
    )
