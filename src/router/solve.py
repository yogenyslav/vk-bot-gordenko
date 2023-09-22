from vk.router import Router
from vk.types.message import MessageNewEvent
from data.fake_db import test_categories, tests, state

router = Router()


@router(text=test_categories)
async def process_category(event: MessageNewEvent):
    if state[event.from_user.id]["action"] == "choosing_category":
        category = event.object.message.text
        if category in tests.keys():
            reply = f"{tests[category].tasks[0]}"
            state[event.from_user.id]["action"] = "solving"
            return await event.answer(text=reply)
