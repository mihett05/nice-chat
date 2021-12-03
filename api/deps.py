from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from core import get_settings, SessionLocal
from core.auth import oauth2_scheme, get_user_by_username, ALGORITHM
from core.models import User
from core.schemes.token import TokenData

settings = get_settings()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
    )
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        if payload.get('sub') is None:
            raise error
        token_data = TokenData(**payload)
    except JWTError:
        raise error
    user = get_user_by_username(db, token_data.sub)
    if user is None:
        raise error
    return user
