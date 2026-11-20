from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

# sqlite_file_name = "database.db"
# connection_url example: https://docs.sqlalchemy.org/en/21/dialects/postgresql.html#psycopg
# connection_url = f"postgresql+psycopg://user:password@host:port/dbname[?key=value&key=value...]"
connection_url = f"postgresql+psycopg://user:password@127.0.0.1:5432/test"

engine = create_engine(connection_url)


# session config
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


# Migration of startup
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
