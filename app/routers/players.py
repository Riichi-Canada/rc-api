from typing import Annotated

from fastapi import APIRouter, Response, Query

router = APIRouter(
    prefix='/api/v1/players'
)


@router.get('')
def get_players(score_limit_2025: Annotated[float, Query(ge=0, le=6000)] = 0,
                page: Annotated[int, Query(gt=0)] = 1, per_page: Annotated[int, Query(gt=0)] = 100) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')


@router.get('/{player_id}')
def get_player(player_id: int) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')
