from vk.router import Router
from vk.types.message import MessageNewEvent

router = Router()


@router("Начать")
async def start(event: MessageNewEvent):
    return await event.answer(
        f"Привет, {event.from_user.first_name} {event.from_user.last_name}!"
    )
