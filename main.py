from fastapi import FastAPI, HTTPException
from models import ItemPayload
from routers import books


app = FastAPI()
grocery_list: dict[int, ItemPayload] = {}

app.include_router(books.router)
