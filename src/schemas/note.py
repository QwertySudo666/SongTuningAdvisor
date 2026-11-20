from enum import Enum
from pydantic import BaseModel, Field


class NoteName(str, Enum):
  c = "C"
  c_sharp = "C#"
  d = "D"
  d_sharp = "D#"
  e = "E"
  f = "F"
  f_sharp = "F#"
  g = "G"
  g_sharp = "G#"
  a = "A"
  a_sharp = "A#"
  b = "B"

  b_flat = "Bb"
  d_flat = "Db"
  e_flat = "Eb"
  g_flat = "Gb"
  a_flat = "Ab"


class Note(BaseModel):
  name: NoteName
  octave: int = Field(..., ge=0, le=8, examples=[2])
