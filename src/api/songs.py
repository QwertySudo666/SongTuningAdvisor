from typing import Annotated

from fastapi import APIRouter, Depends

from schemas.song_create import SongCreate
from services.song_service import SongService

router = APIRouter()


@router.post("/songs/", tags=["songs"])
def add_song(
        song: SongCreate,
        song_service: Annotated[SongService, Depends(SongService)],
):
    return song_service.add_song(song)


@router.get("/songs/", tags=["songs"])
def get_songs(song_service: Annotated[SongService, Depends(SongService)]):
    return song_service.get_songs()
