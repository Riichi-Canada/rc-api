from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..db.database import get_db
from ..models import Club as ClubModel

router = APIRouter(
    prefix='/api/v1/clubs'
)


class Club(BaseModel):
    id: int
    club_name: str
    club_short_name: str


class Clubs(BaseModel):
    records: list[Club]


@router.get('', response_model=Clubs)
async def get_clubs(db: Session = Depends(get_db)) -> Clubs:
    clubs = db.query(ClubModel).all()
    return Clubs(records=[Club.model_validate(club) for club in clubs])


@router.get('/{club_id}', response_model=Club)
async def get_club(club_id: int, db: Session = Depends(get_db)) -> Club:
    club = db.query(ClubModel).filter(ClubModel.id == club_id).first()
    if club is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No club with id {club_id}')
    return Club.model_validate(club)
