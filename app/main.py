import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

app = FastAPI()

# app.include_router(books.router)


# class BookItem(BaseModel):
#     title: str
#     book_cover: str
#     author: str
#     publisher: str
#     publish_date: str
#     isbn: str
#     description: Optional[str] = None

@app.get("/api/v1/get_book_list")
async def get_book_list():
    return {
        "title":"test",
        "book_cover":"http://www.naver.com",
        "author":"seungha.baek",
        "publish_date":"2024-05-03",
        "isbn":"sdf11133",
        "description":"이것은 테스트입니다.",
    }


@app.post("/api/v1/write_book_review")
async def write_book_review():
    # request body
    return {"result_type": "SUCCESS", "results:": "review done!"}


@app.get("/api/v1/get_book_review")
async def get_book_review():
    return {"result_type": "SUCCESS", "results:": "review done!"}


@app.get("/api/v1/get_reviewer_review_list")
async def get_reviewer_review_list():
    return {"result_type": "SUCCESS", "results:": "review done!"}


handler = Mangum(app)
