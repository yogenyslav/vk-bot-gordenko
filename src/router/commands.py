from vk.router import Router
from vk.types.message import MessageNewEvent
from data.fake_db import test_categories, state
from utils import kb
from utils.logging import get_logger


router = Router()
log = get_logger(__name__)


@router("Начать")
async def start(event: MessageNewEvent):
    user_id = event.from_user.id
    if user_id in state.keys():
        state[user_id]["action"] = "started"
    else:
        state[user_id] = {}
        state[user_id]["action"] = "started"
        state[user_id]["mistakes"] = {}
        state[user_id]["correct"] = {}
    log.debug(f"User {user_id} has started the bot")
    return await event.answer(
        text=f"Привет, {event.from_user.first_name} {event.from_user.last_name}! В этом боте ты можешь решить тесты и посмотреть свою статистику по ним",
        reply_markup=kb.start(),
    )


@router("Решить тесты")
async def solve_tests(event: MessageNewEvent):
    user_id = event.from_user.id
    log.debug(f"User {user_id} is choosing category")
    try:
        if (
            state[user_id]["action"] == "started"
            or state[user_id]["action"].split(",")[0] == "solving"
        ):
            state[user_id]["action"] = "choosing_category"
            return await event.answer(
                text="Выбери категорию",
                reply_markup=kb.categories(test_categories),
            )
    except Exception:
        return


@router("Статистика")
async def statistics(event: MessageNewEvent):
    user_id = event.from_user.id

    log.debug(f"User {user_id} has used 'Статистика'")
    response = ""
    if state[user_id]["correct"] != {}:
        response += "Правильные ответы:\n"
        for category, correct in state[user_id]["correct"].items():
            response += f"{category}: {correct}\n"
        response += "\n"

    if state[user_id]["mistakes"] == {}:
        response += "У тебя нет ошибок!"
    else:
        response += "Твои ошибки:\n"
        for category, mistakes in state[user_id]["mistakes"].items():
            response += f"{category}: {mistakes}\n"
        response += "\n"

    return await event.answer(text=response, reply_markup=kb.start())
