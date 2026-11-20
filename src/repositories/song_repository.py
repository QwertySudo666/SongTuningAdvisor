from typing import Sequence

from sqlmodel import select, Session

from models.song import Song


class SongRepository:

    def add_song(self, song: Song, session: Session):
        session.add(song)

    def get_songs(self, session: Session) -> Sequence[Song]:
        return session.exec(select(Song)).all()
