from pydantic import BaseModel, Field

from schemas.note import Note


class TuningBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, examples=["E Standard"])
    notes: list[Note] = Field(
        ...,
        min_length=4,
        max_length=9,
        examples=[
            [
                {"name": "G#", "octave": 2},
                {"name": "C#", "octave": 3},
                {"name": "F#", "octave": 3},
                {"name": "B", "octave": 3},
                {"name": "D#", "octave": 4},
                {"name": "G#", "octave": 4},
            ]
        ],
    )


class TuningCreate(TuningBase):
    pass


class TuningResponse(TuningBase):
    id: str = Field(..., min_length=36)
