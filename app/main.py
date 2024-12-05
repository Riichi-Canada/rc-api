from fastapi import FastAPI, status, Response

from models import create_database

from routers.clubs import router as clubs_router
from routers.event_results import router as event_results_router
from routers.events import router as events_router
from routers.player_results import router as player_results_router
from routers.players import router as players_router


create_database()

app = FastAPI()

app.include_router(clubs_router)
app.include_router(players_router)
app.include_router(events_router)
app.include_router(event_results_router)
app.include_router(player_results_router)


@app.get('/')
def read_root() -> Response:
    return Response(status_code=status.HTTP_200_OK, content='Server is running')
