import uuid
from typing import Annotated

from fastapi import Depends

from models.song import Song
from repositories.db_config import SessionDep
from repositories.song_repository import SongRepository
from repositories.stats_repository import StatsRepository
from schemas.song_create import SongCreate, SongResponse


class SongService:
    def __init__(
            self,
            session: SessionDep,
            song_repository: Annotated[SongRepository, Depends(SongRepository)],
            stats_repository: Annotated[StatsRepository, Depends(StatsRepository)],
    ):
        self.session = session
        self.song_repository = song_repository
        self.stats_repository = stats_repository

    def add_song(self, song: SongCreate):
        with self.session.begin():
            db_song = Song(
                id=uuid.uuid7().__str__(),
                artist_id=song.artist,
                tuning_id=song.tuning_id,
                title=song.title
            )
            self.song_repository.add_song(db_song, self.session)
            self.stats_repository.update_tuning_stat(db_song, self.session)
        return db_song.id

    def get_songs(self) -> list[SongResponse]:
        db_songs = self.song_repository.get_songs(self.session)
        return [
            SongResponse(
                id=db_song.id.__str__(),
                artist=db_song.artist_id,
                title=db_song.title,
                tuning_id=db_song.tuning_id
            ) for db_song in db_songs]
