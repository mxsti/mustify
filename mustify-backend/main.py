""" main.py  where fast api stuff is created  """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlmodel import select
from app.dbutils import create_db_and_tables, SessionDep
from app.models.song_info import SongInfo

app = FastAPI()
app.mount("/songfiles", StaticFiles(directory="audiofiles"), name="audio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:59553"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/songs/")
def get_songs(session: SessionDep) -> list[SongInfo]:
    """
    get all songs in the database
    :returns a list of all songs
    """
    songs = session.exec(select(SongInfo)).all()
    return songs


@app.post("/songs/")
def create_song(song: SongInfo, session: SessionDep) -> SongInfo:
    """
    create a new song in the database
    :returns the created song
    """
    session.add(song)
    session.commit()
    session.refresh(song)
    return song
