from sqlmodel import SQLModel, Field


class Artist(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
