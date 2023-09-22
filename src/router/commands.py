from vk.router import Router
from vk.types.message import MessageNewEvent
from vk.utils import reply_keyboard, Button


router = Router()


@router("Начать")
async def start(event: MessageNewEvent):
    return await event.answer(
        text=f"Привет, {event.from_user.first_name} {event.from_user.last_name}!",
        reply_markup=reply_keyboard(True, Button(text="Решить тесты")),
    )


@router("Решить тесты")
async def solve_tests(event: MessageNewEvent):
    test_categories = ["Golang", "Функан", "Музыка"]
    return await event.answer(
        text="\n".join(test_categories),
        reply_markup=reply_keyboard(
            True,
            *[Button(text=category) for category in test_categories],
            Button(text="Начать"),
        ),
    )
