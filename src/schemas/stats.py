from pydantic import BaseModel


class UserTuningStatsResponse(BaseModel):
    tuning_name: str
    songs: int