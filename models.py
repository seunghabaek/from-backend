from typing import List
from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


class ItemPayload(BaseModel):
    item_id: Optional[int]
    item_name: str
    quantity: int


@dataclass
class BookItem:
    title: str
    book_cover: str
    author: str
    publisher: str
    publish_date: str
    isbn: str
    description: str


@dataclass
class BookList:
    total: int
    display: int
    items: List
