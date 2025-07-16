from fastapi import FastAPI, status, Response, Depends, HTTPException

from app.models import create_database

from app.authentication import validate_api_key

from app.routers.clubs import router as clubs_router
from app.routers.event_results import router as event_results_router
from app.routers.events import router as events_router
from app.routers.player_results import router as player_results_router
from app.routers.players import router as players_router

create_database()

app = FastAPI()

app.include_router(clubs_router)
app.include_router(players_router)
app.include_router(events_router)
app.include_router(event_results_router)
app.include_router(player_results_router)


@app.get('/')
def read_root(_: str = Depends(validate_api_key)) -> Response:
    content = f'Server is running.'
    return Response(status_code=status.HTTP_200_OK, content=content)
