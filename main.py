import json
import os
import requests

from fastapi import FastAPI, HTTPException, Header, Depends
from domain.books.books_service import get_naver_books_list
# from domain.books.books_service import get_naver_books_list
from models import ItemPayload
from routers import books

from dotenv import load_dotenv

app = FastAPI()
grocery_list: dict[int, ItemPayload] = {}

app.include_router(books.router)

load_dotenv()

# import env file
X_NAVER_CLIENT_ID = os.getenv("X_NAVER_CLIENT_ID")
X_NAVER_CLIENT_SECRET = os.getenv("X_NAVER_CLIENT_SECRET")

headers = {"X-Naver-Client-Id": X_NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": X_NAVER_CLIENT_SECRET}

@app.get("/get_book_list_test")
async def root():
    response = get_naver_books_list(query="love", display=10, sort="sim", header_dict=headers)
    return response
