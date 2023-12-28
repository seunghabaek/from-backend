import os

from fastapi import APIRouter, Depends, Header
from typing import Union

from dotenv import load_dotenv

from domain.books.books_service import get_naver_books_list

load_dotenv()

X_NAVER_CLIENT_ID = os.getenv("X_NAVER_CLIENT_ID")
X_NAVER_CLIENT_SECRET = os.getenv("X_NAVER_CLIENT_SECRET")

header_dict = {"X-Naver-Client-Id": X_NAVER_CLIENT_ID, "X-Naver-Client-Secret":X_NAVER_CLIENT_SECRET}


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
    
    return {"books" : response} # type: ignore


@router.get("/")
async def root():
    return {"message": f"{X_NAVER_CLIENT_ID}"}

