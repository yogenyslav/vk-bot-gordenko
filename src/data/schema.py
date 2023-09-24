from pydantic import BaseModel


class Task(BaseModel):
    text: str
    answer: str
    options: list[str]
    docs: str
