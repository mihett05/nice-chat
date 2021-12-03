from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from passlib.context import CryptContext

from core import get_settings
from core.models import User
from core.schemes.token import TokenData

settings = get_settings()
ALGORITHM = "HS256"
TOKEN_EXPIRE = timedelta(hours=48)

pwd_context = CryptContext(schemes=["bcrypt"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter_by(id=user_id).first()


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter_by(username=username).first()
    if user and verify_password(password, user.hashed_password):
        return user


def create_access_token(user_id: int) -> str:
    data = {
        "sub": user_id,
        "exp": datetime.utcnow() + TOKEN_EXPIRE
    }
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)
