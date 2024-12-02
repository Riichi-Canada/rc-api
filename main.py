from fastapi import FastAPI
from db_config import DB_NAME, DB_HOST, DB_USER, DB_PASSWORD


DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


app = FastAPI()


@app.get('/')
def read_root() -> dict[str, str]:
    return {'message': 'API is running'}


