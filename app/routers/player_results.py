from fastapi import APIRouter, Response

router = APIRouter(
    prefix='/api/v1/player_results'
)


@router.get('/{player_id}')
def get_club(player_id: int) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')
