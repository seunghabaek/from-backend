
import yaml

from fastapi import APIRouter
from typing import Union

from app.domain.books.books_service import get_naver_books_list, get_book_list_response
from app.models import BookList, BookListResponse


with open("conf.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    x_naver_client_id = config["secrets"]["naver"]["client_id"]
    x_naver_client_secret = config["secrets"]["naver"]["client_secret"]

X_NAVER_CLIENT_ID=x_naver_client_id
X_NAVER_CLIENT_SECRET=x_naver_client_secret


header_dict = {
    "X-Naver-Client-Id": X_NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": X_NAVER_CLIENT_SECRET
}

router = APIRouter(
    prefix="/books",
    tags=["books"],
    # dependencies=[Depends(get_naver_headers)],
)


@router.get("/get_book_list", response_model=BookListResponse)
async def get_book_list(keyword: str):
    display = 10
    sort = "sim"

    response = get_naver_books_list(keyword, display, sort, header_dict)
    book_list_response = get_book_list_response(response)

    # type: ignore
    return {"result_type": "SUCCESS", "results": book_list_response}


@router.post("/write_book_review")
async def write_book_review():
    # request body
    return {"result_type": "SUCCESS", "results:": "review done!"}


@router.get("/get_book_review")
async def get_book_review():
    return {"result_type": "SUCCESS", "results:": "review done!"}


@router.get("/get_reviewer_review_list")
async def get_reviewer_review_list():
    return {"result_type": "SUCCESS", "results:": "review done!"}
