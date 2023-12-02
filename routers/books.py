from fastapi import APIRouter, Depends, Header
from starlette.config import Config

# setup config
config = Config('.env')

def get_naver_headers(
    x_naver_client_id: str = Header(...),
    naver_client_secret: str = Header(...),
):
    return {
        "naver_client_id": x_naver_client_id,
        "naver_client_secret": naver_client_secret,
    }

router = APIRouter(
    prefix="/books",
    tags=["books"],
    dependencies=[Depends(get_naver_headers)],
)

@router.get("/get_book_list")
def get_book_list(headers: dict = Depends(get_naver_headers)) -> dict[str, str]:
    return {"message": "Hello World", "headers": headers} # type: ignore
