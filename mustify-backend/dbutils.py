import os
from typing import Annotated
from fastapi import Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session

load_dotenv()
sqlite_filename = os.environ.get("SQLITE_FILENAME")
sqlite_url = f"sqlite:///{sqlite_filename}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
