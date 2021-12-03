import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')

