import os
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    DEBUG = os.environ.get('DEBUG', True)


@lru_cache()
def get_settings() -> Settings:
    return Settings()
