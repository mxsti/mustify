""" data model for the metadata for a song  """

from sqlmodel import SQLModel, Field
from typing import Optional


class SongInfo(SQLModel, table=True):
    """
    contains all metadata for the song
    """
    id: int | None = Field(default=None, primary_key=True)
    title: str
    filename: str = Field(unique=True, nullable=False)
    artist: Optional[str] = None
    album: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None
    duration: Optional[int] = None
