from fastapi import APIRouter
from .endpoints import users, auth

api = APIRouter()

api.include_router(users.router, prefix='/users')
api.include_router(auth.router, prefix='/auth')
