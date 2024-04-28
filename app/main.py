import os
from fastapi import FastAPI, HTTPException
from mangum import Mangum
# from app.routers import books

app = FastAPI()

# app.include_router(books.router)

@app.get("/")
def read_root():
    return {"test": "FastAPI Running"}

@app.post("/write_book_review")
async def write_book_review():
    # request body
    return {"result_type": "SUCCESS", "results:": "review done!"}


@app.get("/get_book_review")
async def get_book_review():
    return {"result_type": "SUCCESS", "results:": "review done!"}


@app.get("/get_reviewer_review_list")
async def get_reviewer_review_list():
    return {"result_type": "SUCCESS", "results:": "review done!"}


handler = Mangum(app)
