from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str


class LoginResponse(BaseModel):
    message: str
    username: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    due_date: str
    completed: bool