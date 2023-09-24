import asyncio
from vk.router import Router
from vk.types.message import MessageNewEvent, SendMessage
from vk.client import VkClient
from data.fake_db import tests, state
from data.schema import Task
from utils.logging import get_logger
from utils.settings import settings

router = Router()
log = get_logger(__name__)
vk = VkClient(settings.vk_token)


@router(starts_with="Добавить тест")
async def add_new_test(event: MessageNewEvent):
    # ['Добавить тест', '<category>', '<text>', '<options splitted by ,>', '<answer>', '<docs url>]
    try:
        _, category, text, options, answer, docs = event.object.message.text.split("\n")
    except Exception:
        log.debug(
            f"User {event.from_user.id} has tried to add new task: {event.object.message.text}"
        )
        return await event.answer(text="Неверный формат задания!")
    options = options.split(",")
    log.debug(
        f"User {event.from_user.id} has added new task: {event.object.message.text}"
    )

    new_task = Task(text=text, answer=answer, options=options, docs=docs)
    tests[category].append(new_task)

    for user_id in state.keys():
        await vk.send_message(
            SendMessage(
                user_id=user_id, text=f"В категории {category} появился новый тест!"
            )
        )
    log.debug(f"Current users: {state.keys()}")

    return await event.answer(text=f"Добавлен новый тест: {new_task}")
