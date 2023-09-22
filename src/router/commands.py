from vk.router import Router
from vk.types.message import MessageNewEvent
from vk.utils import reply_keyboard, Button
from data.fake_db import test_categories, state


router = Router()


@router("Начать")
async def start(event: MessageNewEvent):
    state[event.from_user.id]["action"] = "started"
    return await event.answer(
        text=f"Привет, {event.from_user.first_name} {event.from_user.last_name}!",
        reply_markup=reply_keyboard(True, Button(text="Решить тесты")),
    )


@router("Решить тесты")
async def solve_tests(event: MessageNewEvent):
    if state[event.from_user.id]["action"] == "started":
        state[event.from_user.id]["action"] = "choosing_category"
        return await event.answer(
            text="\n".join(test_categories),
            reply_markup=reply_keyboard(
                True,
                *[Button(text=category) for category in test_categories],
                Button(text="Начать"),
            ),
        )
