from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[id]
    username: str


class UserCreation(User):
    password: str
