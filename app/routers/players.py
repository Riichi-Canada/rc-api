import datetime as d
from typing import Annotated, Any

from fastapi import APIRouter, HTTPException, status, Depends, Query, Response
from sqlalchemy import asc
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.database import get_db
from app.models import Player as PlayerModel
from app.models import EventResult as ResultModel
from app.models import Event as EventModel
from app.models import EventScores2025 as EventScores2025Model
from app.models import EventScores2028 as EventScores2028Model
from app.models import PlayerScores2025 as PlayerScores2025Model
from app.models import PlayerScores2028 as PlayerScores2028Model
from app.authentication import validate_api_key

router = APIRouter(
    prefix='/api/v1/players'
)

# region PyDantic Models
class Player(BaseModel):
    id: int
    first_name: str
    last_name: str
    player_region: int
    player_club: int | None
    player_score_2025_cycle: float | None
    player_score_2028_cycle: float | None
    event_results: str

class Players(BaseModel):
    records: list[Player]

class Result(BaseModel):
    event_name: str
    placement: int
    score: float | None

class Results (BaseModel):
    records: list[Result]

# class PlayerScores2025(BaseModel):
#     id: int
#     player_id: int
#     total_score: float | None
#
# class Scores2025(BaseModel):
#     records: list[PlayerScores2025]

# endregion PyDantic Models


@router.get('')
async def get_players(
    _: str = Depends(validate_api_key),
    db: Session = Depends(get_db),
) -> Players:
    players = db.query(PlayerModel).order_by(asc(PlayerModel.id)).all()

    data = Players(
        records=[
            Player(
                id=player.id,
                first_name=player.first_name,
                last_name=player.last_name,
                player_region=player.player_region,
                player_club=player.player_club,
                player_score_2025_cycle=player.player_score_2025_cycle,
                player_score_2028_cycle=player.player_score_2028_cycle,
                event_results=f'/players/{player.id}/event_results'
            ) for player in players
        ]
    )

    return data


@router.get('/{player_id}')
async def get_player(
    player_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(validate_api_key)
) -> Player:
    player = db.query(PlayerModel).filter(PlayerModel.id == player_id).first()
    if player is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No player with id {player_id}')

    data = Player(
        id=player.id,
        first_name=player.first_name,
        last_name=player.last_name,
        player_region=player.player_region,
        player_club=player.player_club,
        player_score_2025_cycle=player.player_score_2025_cycle,
        player_score_2028_cycle=player.player_score_2028_cycle,
        event_results=f'/players/{player_id}/event_results'
    )

    return data

@router.get('/{player_id}/event_results')
async def get_player_results(
    player_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(validate_api_key)
) -> Any:
    results = db.query(ResultModel).filter(ResultModel.player_id == player_id).all()

    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No results found for player with id {player_id}')

    records = []

    for result in results:
        event = db.query(EventModel).filter(EventModel.id == result.event_id).first()

        if event.event_start_date >= d.date(2022, 1, 1) and event.event_end_date <= d.date(2024, 12, 31):
            event_rank_points = db.query(EventScores2025Model).filter(
                EventScores2025Model.result_id == result.id).first()

            ranking_points = {
                'main_points': event_rank_points.main_score,
                'tank': event_rank_points.tank_score
            }

            player_scores = db.query(PlayerScores2025Model).filter(
                PlayerScores2025Model.player_id == result.player_id
            ).first()

            counts_for_relevant_cycle = (
                result.id == player_scores.out_of_region_live or
                result.id == player_scores.other_live_1 or
                result.id == player_scores.other_live_2 or
                result.id == player_scores.any_event_1 or
                result.id == player_scores.any_event_2 or
                result.id == player_scores.tank_1 or
                result.id == player_scores.tank_2 or
                result.id == player_scores.tank_3 or
                result.id == player_scores.tank_4 or
                result.id == player_scores.tank_5
            )

        elif event.event_start_date >= d.date(2025, 1, 1) and event.event_end_date <= d.date(2027, 12, 31):
            event_rank_points = db.query(EventScores2028Model).filter(
                EventScores2028Model.result_id == result.id
            ).first()

            ranking_points = {
                'part_A': event_rank_points.part_a,
                'part_B': event_rank_points.part_b
            }

            player_scores = db.query(PlayerScores2028Model).filter(
                PlayerScores2028Model.player_id == result.player_id
            ).first()

            counts_for_relevant_cycle = (
                    result.id == player_scores.slot_1 or
                    result.id == player_scores.slot_2 or
                    result.id == player_scores.slot_3 or
                    result.id == player_scores.slot_4 or
                    result.id == player_scores.slot_5
            )

        else:  # Event is from earlier than 2022, when Canada had no formalized ranking system
            ranking_points = {}
            counts_for_relevant_cycle = False

        result_data = {
            'event_details': {
                'event_name': event.event_name,
                'event_region': event.event_region,
                'event_type': event.event_type,
                'event_start_date': event.event_start_date,
                'event_end_date': event.event_end_date,
                'event_city': event.event_city,
                'event_country': event.event_country,
                'number_of_players': event.number_of_players,
                'event_is_online': event.is_online,
                'event_ruleset': event.event_ruleset
            },
            'result_details': {
                'placement': result.placement,
                'score': result.score,
                'ranking_points': ranking_points,
                'counts_for_relevant_cycle': counts_for_relevant_cycle
            }
        }

        records.append(result_data)

    return records
