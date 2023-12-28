import os

from fastapi import FastAPI, HTTPException

from routers import books

app = FastAPI()

app.include_router(books.router)
