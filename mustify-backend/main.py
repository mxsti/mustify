""" main.py for where fast api stuff is created  """

from fastapi import FastAPI
from dbutils import create_db_and_tables, SessionDep
from models.song_info import SongInfo

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.post("/song/")
def create_hero(song: SongInfo, session: SessionDep) -> SongInfo:
    session.add(song)
    session.commit()
    session.refresh(song)
    return song
