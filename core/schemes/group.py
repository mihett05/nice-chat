from pydantic import BaseModel
from typing import List


class Group(BaseModel):
    name: str


class GroupInDb(Group):
    id: int
    admin: int
    members: List[int]

    class Config:
        orm_mode = True
