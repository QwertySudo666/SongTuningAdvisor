from pydantic import BaseModel, Field

from schemas.note import Note


class SongBase(BaseModel):
    artist: str = Field(..., min_length=1, max_length=200, examples=["Metallica"])
    title: str = Field(..., min_length=1, max_length=200, examples=["Master of Puppets"])
    tuning_id: str = Field(..., min_length=36, max_length=36, examples=["b68a0ee3-25e8-40d3-873a-a5e1276c32b5"])


class SongCreate(SongBase):
    pass


class SongResponse(SongBase):
    id: str
    # user_id: int add later

    class Config:
        from_attributes = True
