from pydantic import BaseModel


class Task(BaseModel):
    text: str
    answer: str


class Test(BaseModel):
    category: str
    tasks: list[Task]
