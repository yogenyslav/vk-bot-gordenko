from vk.utils import reply_keyboard, Button
from data.schema import Task


def start():
    return reply_keyboard(True, Button(text="Решить тесты"), Button(text="Статистика"))


def categories(test_categories: list[str]):
    return reply_keyboard(
        True,
        *[Button(text=category) for category in test_categories],
        Button(text="Начать"),
    )


def task_options(task: Task):
    return reply_keyboard(True, *[Button(text=option) for option in task.options])
