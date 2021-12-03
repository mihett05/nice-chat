from typing import Optional
from pydantic import BaseModel


class TokenData(BaseModel):
    sub: Optional[str]


class TokenResponse(BaseModel):
    access_token: str
    user_id: int
    username: str
