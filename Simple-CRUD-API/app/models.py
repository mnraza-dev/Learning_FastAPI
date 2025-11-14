from pydantic import BaseModel

class Task(BaseModel):
    title: str
    isCompleted: bool = False
