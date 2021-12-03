from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from core import SessionLocal
from core.auth import authenticate_user, create_access_token, create_user
from core.schemes.user import UserCreation
from core.schemes.token import TokenResponse
from api.deps import get_db

router = APIRouter()


@router.post('/register', response_model=TokenResponse)
def register(form: UserCreation, db: SessionLocal = Depends(get_db)):
    user = create_user(db, form.username, form.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username is taken"
        )
    token = create_access_token(user.username)
    return {
        "access_token": token,
        "user_id": user.id,
        "username": user.username
    }


@router.post('/login', response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login data"
        )
    token = create_access_token(user.username)
    return {
        "access_token": token,
        "user_id": user.id,
        "username": user.username
    }
