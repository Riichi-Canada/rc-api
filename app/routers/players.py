from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Query, Response
from sqlalchemy import asc
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.database import get_db
from app.models import Player as PlayerModel
from app.models import EventResult as ResultModel
from app.authentication import validate_api_key

router = APIRouter(
    prefix='/api/v1/players'
)

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
) -> Results:
    results = db.query(ResultModel).filter(ResultModel.player_id == player_id).all()

    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No results found for player with id {player_id}')

    data = Results(
        records=[
            Result(event_name=str(result.event_id), placement=result.placement, score=result.score) for result in results
        ]
    )
    return data
