import datetime
from typing import Annotated
from fastapi import APIRouter, Response, Query

router = APIRouter(
    prefix='/api/v1/events'
)


@router.get('')
def get_events(
        event_region: Annotated[list[int] | None, Query(gt=0)] = None,
        event_type: Annotated[int | None, Query(gt=0)] = None, event_city: str | None = None,
        event_country: str | None = None, online: bool | None = None,
        minimum_player_count: Annotated[int, Query(gt=0)] = 1,
        from_date: datetime = datetime.date(2000, 1, 1), until_date: datetime = datetime.date.today(),
        page: Annotated[int, Query(gt=0)] = 1, per_page: Annotated[int, Query(gt=0)] = 100) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')


@router.get('/{event_id}')
def get_event(event_id: int) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')
