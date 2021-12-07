from fastapi import APIRouter
from .endpoints import users, auth, messages

api = APIRouter()

api.include_router(users.router, prefix='/users')
api.include_router(auth.router, prefix='/auth')
api.include_router(messages.app, prefix='/msg')
