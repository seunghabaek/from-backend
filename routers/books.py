import os

from fastapi import APIRouter, Depends, Header
from typing import Union

from dotenv import load_dotenv

from domain.books.books_service import get_naver_books_list
from models import BookItem,  BookList

load_dotenv()

X_NAVER_CLIENT_ID = os.getenv("X_NAVER_CLIENT_ID")
X_NAVER_CLIENT_SECRET = os.getenv("X_NAVER_CLIENT_SECRET")

header_dict = {
    "X-Naver-Client-Id": X_NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": X_NAVER_CLIENT_SECRET
}

router = APIRouter(
    prefix="/books",
    tags=["books"],
    # dependencies=[Depends(get_naver_headers)],
)


@router.get("/get_book_list")
async def get_book_list(keyword: str):
    display = 10
    sort = "sim"
    response = get_naver_books_list(keyword, display, sort, header_dict)

    # argument
    response_total = response.get("total")
    items = response.get("items")

    items_list = [
        BookItem(
            title=item.get("title"),
            book_cover=item.get("image"),
            author=item.get("author"),
            publisher=item.get("publisher"),
            publish_date=item.get("pubdate"),
            isbn=item.get("isbn"),
            description=item.get("description"),
        ) for item in items
    ]

    book_list_response = BookList(
        total=response.get("total"),
        display=response.get("display"),
        items=items_list)

    return {"books": book_list_response}  # type: ignore
