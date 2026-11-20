from sqlmodel import select, Session

from models.tuning import Tuning
from repositories.db_config import SessionDep


class TuningRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def save(self, db_tuning, session: Session):
        session.add(db_tuning)

    def fetch_all(self, session: Session):
        return session.exec(select(Tuning)).all()
