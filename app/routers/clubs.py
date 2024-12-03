from fastapi import APIRouter, Response

router = APIRouter(
    prefix='/api/v1/clubs'
)


@router.get('')
def get_clubs() -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')


@router.get('/{club_id}')
def get_club(club_id: int) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')
