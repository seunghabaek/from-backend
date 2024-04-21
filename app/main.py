import os
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from app.routers import books

app = FastAPI()

app.include_router(books.router)

handler = Mangum(app)
