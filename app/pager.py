from typing import Any
from fastapi import HTTPException
from starlette import status


def paginate(query, route: str, page: int, per_page: int) -> dict[str, Any]:
    total_count = query.count()
    page_count = (total_count + per_page - 1) // per_page

    if page > page_count:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Page is too high (expected <={page_count}, got {page})')

    records = query.offset((page - 1) * per_page).limit(per_page).all()

    metadata = {
        "page": page,
        "per_page": per_page,
        "page_count": page_count,
        "total_count": total_count,
        "links": [
            {"self": f"/{route}?page={page}&per_page={per_page}"},
            {"first": f"/{route}?page=1&per_page={per_page}"},
            {"previous": f"/{route}?page={max(1, page - 1)}&per_page={per_page}"},
            {"next": f"/{route}?page={min(page + 1, page_count)}&per_page={per_page}"},
            {"last": f"/{route}?page={page_count}&per_page={per_page}"}
        ]
    }

    return {
        "metadata": metadata,
        "records": records
    }
