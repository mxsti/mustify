""" data model for the metadata for a song  """

from sqlmodel import SQLModel, Field


class SongInfo(SQLModel, table=True):
    """
    contains all metadata for the song
    """
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    album: str
    genre: str
    year: int
    duration: int
