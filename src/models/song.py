from sqlmodel import SQLModel, Field


class Song(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    artist_id: str = Field(index=True)
    tuning_id: str = Field(index=True)
    title: str = Field(index=True)
