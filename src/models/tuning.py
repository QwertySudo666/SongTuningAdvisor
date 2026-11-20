from sqlmodel import SQLModel, Field, Column, JSON


class Tuning(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    notes: list[dict] = Field(sa_column=Column(JSON))
