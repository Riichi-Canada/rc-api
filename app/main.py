from fastapi import FastAPI, Response
from db_config import DB_NAME, DB_HOST, DB_USER, DB_PASSWORD


DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

app = FastAPI()


@app.get('/')
def read_root() -> Response:
    return Response(status_code=200, content='API is running')
