from random import choice
from vk.router import Router
from vk.types.message import MessageNewEvent
from data.fake_db import test_categories, tests, state
from utils import kb
from utils.logging import get_logger

router = Router()
log = get_logger(__name__)


@router(text=test_categories)
async def process_category(event: MessageNewEvent):
    user_id = event.from_user.id
    log.debug(f"User {user_id} has chosen {event.object.message.text} category")
    try:
        if state[user_id]["action"] == "choosing_category":
            category = event.object.message.text
            if category in tests.keys():
                task = choice(tests[category])
                state[user_id]["action"] = f"solving,{category}"
                state[user_id]["task"] = task
                return await event.answer(
                    text=task.text,
                    reply_markup=kb.task_options(task),
                )
    except Exception:
        return


@router(text="test_answer")
async def process_task_answer(event: MessageNewEvent):
    user_id = event.from_user.id
    try:
        action, category = state[user_id]["action"].split(",")
        log.debug(
            f"User {user_id} has answered '{event.object.message.text.lower()}' to task {tests[category]}"
        )
        if action == "solving":
            task = state[user_id]["task"]
            state[user_id]["action"] = "solved"
            if task.answer.lower() != event.object.message.text.lower():
                if category in state[user_id]["mistakes"].keys():
                    state[user_id]["mistakes"][category] += 1
                else:
                    state[user_id]["mistakes"][category] = 1
                return await event.answer(
                    f"Ошибка! Правильный ответ: {task.answer}\nПрочитай этот материал, чтобы не допускать ошибок: {task.docs}",
                    reply_markup=kb.start(),
                )
            else:
                if category in state[user_id]["correct"].keys():
                    state[user_id]["correct"][category] += 1
                else:
                    state[user_id]["correct"][category] = 1
                return await event.answer(
                    "Молодец, это правильный ответ!", reply_markup=kb.start()
                )
    except Exception:
        return
