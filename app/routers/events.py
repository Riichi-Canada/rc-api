from typing import Annotated, Optional
from fastapi import APIRouter, Response, Query
from starlette.responses import JSONResponse
from starlette.status import HTTP_501_NOT_IMPLEMENTED, HTTP_200_OK
import datetime as d
from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Query
from sqlalchemy import asc
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.models import Event as EventModel
from app.models import Ruleset as RulesetModel
from app.authentication import validate_api_key
from app.db.database import get_db
from app.pager import paginate

router = APIRouter(
    prefix='/api/v1/events'
)

# region PyDantic Models
class Ruleset(BaseModel):
    id: int
    name: str

class Event(BaseModel):
    id: int
    event_code: str
    event_name: str
    event_region: int | None
    event_type: int
    event_start_date: str
    event_end_date: str
    event_city: str | None
    event_country: str
    number_of_players: int
    is_online: bool
    event_ruleset: Ruleset
    rule_modifications: str | None
    event_notes: str | None
# endregion PyDantic Models


@router.get('')
def get_events(
        event_region: Annotated[list[int] | None, Query()] = None,
        event_type: Annotated[int | None, Query(gt=0)] = None,
        event_city: str | None = None,
        event_country: str | None = None,
        online: bool | None = None,
        minimum_player_count: Annotated[int, Query(gt=0)] = 1,
        from_date: d.date = d.date(2000, 1, 1),
        until_date: d.date = d.date.today(),
        page: Annotated[int, Query(gt=0)] = 1,
        per_page: Annotated[int, Query(gt=0)] = 100,
        _: str = Depends(validate_api_key),
        db: Session = Depends(get_db),
) -> Response:
    query = db.query(EventModel).order_by(asc(EventModel.event_start_date))

    # region Handling query parameters
    params_string = ''

    if event_region:
        query = query.filter(EventModel.event_region.in_(event_region))
        params_string += '&event_region='
        for region in event_region:
            params_string += f'{region},'
        params_string = params_string.rstrip(',')

    if event_type:
        query = query.filter(EventModel.event_type == event_type)
        params_string += f'&event_type={event_type}'

    if event_city:
        query = query.filter(EventModel.event_city == event_city)
        params_string += f'&event_city={event_city}'

    if event_country:
        query = query.filter(EventModel.event_country == event_country)
        params_string += f'&event_country={event_country}'

    if online is not None:
        query = query.filter(EventModel.is_online == online)
        params_string += f'&online={online}'

    query = query.filter(EventModel.number_of_players >= minimum_player_count)
    params_string += f'&minimum_player_count={minimum_player_count}'

    query = query.filter(EventModel.event_end_date >= from_date, EventModel.event_end_date <= until_date)
    params_string += f'&from_date={from_date}&until_date={until_date}'
    # endregion Handling query parameters

    paginated_data = paginate(query=query, route='events', page=page, per_page=per_page, extra_params=params_string)

    records = []

    for event in paginated_data['records']:
        ruleset = db.query(RulesetModel).filter(RulesetModel.id == event.event_ruleset).first()
        event_ruleset = Ruleset(id=ruleset.id, name=ruleset.name)

        records.append(
            Event(
                id=event.id,
                event_code=event.event_code,
                event_name=event.event_name,
                event_region=event.event_region,
                event_type=event.event_type,
                event_start_date=event.event_start_date.strftime('%Y-%m-%d'),
                event_end_date=event.event_end_date.strftime('%Y-%m-%d'),
                event_city=event.event_city,
                event_country=event.event_country,
                number_of_players=event.number_of_players,
                is_online=event.is_online,
                event_ruleset=event_ruleset,
                rule_modifications=event.rule_modifications,
                event_notes=event.event_notes
            ).model_dump()
        )

    paginated_data['metadata']['filters'] = {
        "event_region": event_region,
        "event_type": event_type,
        "event_city": event_city,
        "event_country": event_country,
        "online": online,
        "minimum_player_count": minimum_player_count,
        "from_date": from_date.strftime('%Y-%m-%d'),
        "until_date": until_date.strftime('%Y-%m-%d'),
    }
    paginated_data['records'] = records

    return JSONResponse(status_code=HTTP_200_OK, content=paginated_data)


@router.get('/{event_id}')
def get_event(event_id: int) -> Response:
    return Response(status_code=HTTP_501_NOT_IMPLEMENTED, content='This route has not yet been implemented')


@router.get('/{event_id}/results')
def get_event_results(event_id: int) -> Response:
    return Response(status_code=HTTP_501_NOT_IMPLEMENTED, content='This route has not yet been implemented')
