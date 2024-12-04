from fastapi import FastAPI, Response
from db_config import DB_NAME, DB_HOST, DB_USER, DB_PASSWORD

from routers.clubs import router as clubs_router
from routers.event_results import router as event_results_router
from routers.events import router as events_router
from routers.player_results import router as player_results_router
from routers.players import router as players_router


DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

app = FastAPI()

app.include_router(clubs_router)
app.include_router(players_router)
app.include_router(events_router)
app.include_router(event_results_router)
app.include_router(player_results_router)


@app.get('/')
def read_root() -> Response:
    return Response(status_code=200, content='Server is running')
