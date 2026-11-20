from typing import Annotated

from fastapi import APIRouter, Depends

from schemas.tuning import TuningBase, TuningCreate
from services import tuning_service
from services.tuning_service import TuningService

router = APIRouter()


@router.post("/tunings/", tags=["tunings"])
def add_tuning(
        tuning: TuningCreate,
        tuning_service: Annotated[TuningService, Depends(TuningService)],
):
    return tuning_service.add_tuning(tuning)


@router.get("/tunings/", tags=["tunings"])
def get_tunings(tuning_service: Annotated[TuningService, Depends(TuningService)]):
    return tuning_service.get_tunings()

@router.get("/tunings/stats", tags=["tunings"])
def get_stats(tuning_service: Annotated[TuningService, Depends(TuningService)]):
    return tuning_service.get_stats()