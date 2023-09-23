from pydantic import BaseModel


class Task(BaseModel):
    text: str
    answer: str
    options: list[str]
    docs: str


class Test(BaseModel):
    category: str
    task: Task
