from typing import Any
from data import schema

test_categories = ["Golang", "Функан", "Музыка"]

tests = {
    "Golang": schema.Test(
        category="Golang",
        tasks=[
            schema.Task(
                text="Как называется функция, которая может выполняться конкурентно?",
                answer="Goroutine",
            )
        ],
    )
}

state: dict[int, dict[str, Any]] = {}
