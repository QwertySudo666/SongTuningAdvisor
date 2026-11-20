import uuid
from typing import Annotated

from fastapi import Depends

from models.tuning import Tuning
from repositories.db_config import SessionDep
from repositories.stats_repository import StatsRepository
from repositories.tuning_repository import TuningRepository
from schemas.note import Note
from schemas.tuning import TuningCreate, TuningResponse


class TuningService:
    def __init__(
            self,
            session: SessionDep,
            tuning_repository: Annotated[TuningRepository, Depends(TuningRepository)],
            stats_repository: Annotated[StatsRepository, Depends(StatsRepository)],
    ):
        self.session = session
        self.tuning_repository = tuning_repository
        self.stats_repository = stats_repository

    def add_tuning(self, tuning: TuningCreate) -> TuningResponse:
        with self.session.begin():
            notes_for_db = [note.model_dump(mode='json') for note in tuning.notes]
            db_tuning = Tuning(
                id=str(uuid.uuid7()),
                name=tuning.name,
                notes=notes_for_db
            )

            # TODO: Check whether tuning exists
            self.tuning_repository.save(db_tuning, self.session)

        return TuningResponse(
            id=db_tuning.id,
            name=db_tuning.name,
            notes=tuning.notes
        )

    def get_tunings(self) -> list[TuningResponse]:
        db_tunings = self.tuning_repository.fetch_all(self.session)
        response_tunings = [TuningResponse(
            id=db_tuning.id,
            name=db_tuning.name,
            notes=[Note(**note) for note in db_tuning.notes]
        ) for db_tuning in db_tunings]
        return response_tunings

    def get_stats(self):
        return self.stats_repository.fetch_all(self.session)

