import os
from fastapi import FastAPI, HTTPException

from app.routers import books

app = FastAPI()

app.include_router(books.router)
