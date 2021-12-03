from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt
from passlib.context import CryptContext

from core import get_settings
from core.models import User

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


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter_by(username=username).first()


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter_by(username=username).first()
    if user and verify_password(password, user.hashed_password):
        return user


def create_access_token(username: str) -> str:
    data = {
        "sub": username,
        "exp": datetime.utcnow() + TOKEN_EXPIRE
    }
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)


def create_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter_by(username=username).first()
    if user is None:
        user = User(username=username, hashed_password=hash_password(password))
        db.add(user)
        db.commit()
        return user
