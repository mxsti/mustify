""" main.py  where fast api stuff is created  """

from fastapi import FastAPI
from app.dbutils import create_db_and_tables, SessionDep
from app.models.song_info import SongInfo
app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    handles everything that should be done on the initial startup of the fastapi instance:
        - creating sql tables
    """
    create_db_and_tables()


@app.get("/")
def hello():
    """ hello world """
    return {"message": "Hello World"}


@app.post("/song/")
def create_hero(song: SongInfo, session: SessionDep) -> SongInfo:
    """
    create a new song in the database
    :returns the created song
    """
    session.add(song)
    session.commit()
    session.refresh(song)
    return song
