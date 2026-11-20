from fastapi import FastAPI

from api import songs
from api import tunings
from repositories.db_config import create_db_and_tables

from models.song import Song
from models.artist import Artist
from models.tuning import Tuning

app = FastAPI()

app.include_router(songs.router)
app.include_router(tunings.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}
