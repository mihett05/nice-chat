from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserCreation(User):
    password: str


class UserInDb(User):
    id: int

    class Config:
        orm_mode = True
