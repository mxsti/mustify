""" utils to create db session and connection for fastapi """

import os
from typing import Annotated
from fastapi import Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session

load_dotenv()
SQLITE_FILENAME = os.environ.get("SQLITE_FILENAME")
SQLITE_URL = f"sqlite:///{SQLITE_FILENAME}"

connect_args = {"check_same_thread": False}
engine = create_engine(SQLITE_URL, connect_args=connect_args)


def create_db_and_tables():
    """
    creating all database tables defined in the SQLModel models
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """
    generator function that yields a database session
    :return:
    """
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
