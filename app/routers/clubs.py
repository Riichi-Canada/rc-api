from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.database import get_db
from app.models import Club as ClubModel

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
    data = Clubs(
        records=[
            Club(id=club.id, club_name=club.club_name, club_short_name=club.club_short_name) for club in clubs
        ]
    )
    return data


@router.get('/{club_id}', response_model=Club)
async def get_club(club_id: int, db: Session = Depends(get_db)) -> Club:
    club = db.query(ClubModel).filter(ClubModel.id == club_id).first()
    if club is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No club with id {club_id}')

    data = Club(id=club.id, club_name=club.club_name, club_short_name=club.club_short_name)
    return data
