from fastapi import APIRouter, Depends
from core.models import User
from core.schemes.user import UserInDb
from api.deps import get_current_user

router = APIRouter()


@router.get('/me', response_model=UserInDb)
def get_me(user: User = Depends(get_current_user)):
    return UserInDb.from_orm(user)


@router.get('/{user_id}')
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
