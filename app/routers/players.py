from fastapi import APIRouter, Response

router = APIRouter(
    prefix='/api/v1/players'
)


@router.get('')
def get_players() -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')


@router.get('/{player_id}')
def get_player(player_id: int) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')
