import uuid
from select import select
from typing import Any, Sequence

from sqlalchemy import Row, text
from sqlalchemy.dialects.postgresql import insert
from sqlmodel import Session

from models.song import Song
from models.user_tuning_stat import UserTuningStat
from schemas.stats import UserTuningStatsResponse


class StatsRepository:

    def update_tuning_stat(self, db_song: Song, session: Session):
        insert_stmt = insert(UserTuningStat).values(
            user_id="01a11165-0000-0000-0000-6fd1ae6ef4f4", # change later
            tuning_id=db_song.tuning_id,
            songs=1
        )

        upsert_stmt = insert_stmt.on_conflict_do_update(
            constraint="uq_user_tuning",
            set_={
                "songs": UserTuningStat.songs + 1
            }
        )

        session.exec(upsert_stmt)

    def fetch_all(self, session: Session) -> Sequence[UserTuningStatsResponse]:
        query = text(
            """
            SELECT t.name AS tuning_name, u.songs
            FROM usertuningstat u
            JOIN tuning t ON t.id = u.tuning_id
            """
        )
        raw_results = session.exec(query).mappings().all()

        return [UserTuningStatsResponse(**row) for row in raw_results]
