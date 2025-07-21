from typing import Annotated, Optional
import datetime as d

from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from fastapi import APIRouter, status, Depends, Query, Response
from sqlalchemy import asc
from sqlalchemy.orm import Session
from pydantic import BaseModel, conint

from app.models import Event as EventModel
from app.models import Ruleset as RulesetModel
from app.models import EventResult as ResultModel
from app.models import EventScores2025 as EventScores2025Model
from app.models import EventScores2028 as EventScores2028Model
from app.models import Club as ClubModel
from app.models import Player as PlayerModel
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
    results: Optional[str]

class EventResult(BaseModel):
    placement: int
    player_id: int | None
    player_first_name: str
    player_last_name: str
    player_region: int | None
    player_club: int | None
    event_points: float
    ranking_points: float | None

class EventResults(BaseModel):
    results: list[EventResult]
    represented_regions: list
    represented_clubs: list
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
def get_event(
        event_id: conint(gt=0),
        _: str = Depends(validate_api_key),
        db: Session = Depends(get_db)
) -> JSONResponse:
    event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if event is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': f'No event with id {event_id}'})

    ruleset = db.query(RulesetModel).filter(RulesetModel.id == event.event_ruleset).first()
    event_ruleset = Ruleset(id=ruleset.id, name=ruleset.name)

    data = Event(
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
        event_notes=event.event_notes,
        results=f'/events/{event_id}/results'
    ).model_dump()

    return JSONResponse(status_code=HTTP_200_OK, content=data)


@router.get('/{event_id}/results')
def get_event_results(
        event_id: conint(gt=0),
        _: str = Depends(validate_api_key),
        db: Session = Depends(get_db)
) -> Response:
    results_data = db.query(ResultModel).filter(ResultModel.event_id == event_id).order_by(asc(ResultModel.placement))

    represented_regions = {}
    represented_clubs = {}

    results = []

    for result in results_data:
        # region Player info
        player = db.query(PlayerModel).filter(PlayerModel.id == result.player_id).first()

        player_region = player.player_region if player else None
        player_club = player.player_club if player else None
        # endregion Player info

        # region Ranking points
        if player:
            event = db.query(EventModel).filter(EventModel.id == result.event_id).first()

            if event.event_start_date >= d.date(2022, 1, 1) and event.event_end_date <= d.date(2024, 12, 31):
                ranking_score_data = db.query(
                    EventScores2025Model
                ).filter(
                    EventScores2025Model.result_id == result.id
                ).first()

                ranking_points = ranking_score_data.main_score + ranking_score_data.tank_score

            elif event.event_start_date >= d.date(2025, 1, 1) and event.event_end_date <= d.date(2027, 12, 31):
                ranking_score_data = db.query(
                    EventScores2028Model
                ).filter(
                    EventScores2028Model.result_id == result.id
                ).first()

                ranking_points = ranking_score_data.part_a + ranking_score_data.part_b

            else:
                ranking_points = None
        else:
            ranking_points = None
        # endregion Ranking points

        # region Update represented_regions
        if player_region in represented_regions:
            represented_regions[player_region] += 1
        else:
            represented_regions[player_region] = 1
        # endregion Update represented_regions

        # region Update represented_clubs
        if player_club is not None:
            club = db.query(ClubModel).filter(ClubModel.id == player_club).first()
            if club:
                club_info = {
                    'id': club.id,
                    'name': club.club_name,
                    'short_name': club.club_short_name
                }
                if club_info['id'] in represented_clubs:
                    represented_clubs[club_info['id']]['number_of_occurences'] += 1
                else:
                    club_info['number_of_occurences'] = 1
                    represented_clubs[club_info['id']] = club_info
        # endregion Update represented_clubs

        results.append(
            EventResult(
                placement=result.placement,
                player_id=result.player_id,
                player_first_name=result.player_first_name,
                player_last_name=result.player_last_name,
                player_region=player_region,
                player_club=player_club,
                event_points=result.score,
                ranking_points=ranking_points
            )
        )

    represented_regions = sorted(represented_regions.items(), key=lambda x: x[1], reverse=True)
    represented_clubs = sorted(represented_clubs.values(), key=lambda x: x['number_of_occurences'], reverse=True)

    represented_regions_sorted = [
        {'region': region, 'number_of_occurences': count}
        for region, count in represented_regions
    ]
    represented_clubs_sorted = [
        {
            'id': club['id'],
            'name': club['name'],
            'short_name': club['short_name'],
            'number_of_occurences': club['number_of_occurences']
        } for club in represented_clubs
    ]

    return_data = EventResults(
        results=results, represented_regions=represented_regions_sorted, represented_clubs=represented_clubs_sorted
    ).model_dump()

    return JSONResponse(status_code=HTTP_200_OK, content=return_data)


















