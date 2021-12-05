from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.models import User
from core.schemes.user import UserInDb
from api.deps import get_current_user, get_db

router = APIRouter()


@router.get('/me', response_model=UserInDb)
def get_me(user: User = Depends(get_current_user)):
    return UserInDb.from_orm(user)


@router.get('/{user_id}')
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(user_id=user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return UserInDb.from_orm(user)
