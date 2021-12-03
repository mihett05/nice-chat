from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from core.settings import get_settings
from core.database import Base, engine
from api.api import api

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)


@app.on_event('start')
def on_start():
    Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api, prefix='/api')

if __name__ == '__main__':
    run('main:app', reload=settings.DEBUG, debug=settings.DEBUG, port=8000)
