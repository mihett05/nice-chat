from typing import Optional
from pydantic import BaseModel


class TokenData(BaseModel):
    sub: Optional[int]
