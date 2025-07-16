from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from app.api_key import API_KEY

header_scheme = APIKeyHeader(name='rc-api-key')


async def validate_api_key(api_key: str = Depends(header_scheme)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid API key'
        )
