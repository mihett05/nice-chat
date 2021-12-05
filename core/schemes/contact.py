from pydantic import BaseModel


class Group(BaseModel):
    contact_id: int
    user_id: int


class GroupInDb(Group):
    id: int

    class Config:
        orm_mode = True
