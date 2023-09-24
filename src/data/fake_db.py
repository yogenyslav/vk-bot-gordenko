from typing import Any
from data import schema

test_categories = ["Golang", "Функан"]

tests = {
    "Golang": [
        schema.Task(
            text="Как называется функция, которая может выполняться конкурентно?",
            answer="Goroutine",
            options=["Goroutine", "Coroutine"],
            docs="https://go.dev/tour/concurrency/1",
        )
    ],
    "Функан": [
        schema.Task(
            text="Обобщение 'длины вектора', заданное в виде функционала - это",
            answer="Норма",
            options=["Модуль", "Норма", "Интеграл"],
            docs="https://ru.wikipedia.org/wiki/%D0%9D%D0%BE%D1%80%D0%BC%D0%B0_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0)",
        )
    ],
}

state: dict[int, dict[str, Any]] = {}
