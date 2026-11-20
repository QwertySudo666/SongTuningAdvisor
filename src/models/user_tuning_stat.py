from sqlalchemy import UniqueConstraint
from sqlmodel import SQLModel, Field


class UserTuningStat(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("user_id", "tuning_id", name="uq_user_tuning"),
    )

    user_id: str | None = Field(default=None, primary_key=True)
    tuning_id: str | None = Field(default=None, primary_key=True)
    songs: int = Field(default=0)
