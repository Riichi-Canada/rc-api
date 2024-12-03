from fastapi import APIRouter, Response

router = APIRouter(
    prefix='/api/v1/event_results'
)


@router.get('')
def get_clubs() -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')


@router.get('/{event_id}')
def get_club(event_id: int) -> Response:
    return Response(status_code=501, content='This route has not yet been implemented')
