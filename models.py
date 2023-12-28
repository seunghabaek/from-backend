from typing import List
from dataclasses import dataclass


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
    items: List[BookItem]


@dataclass
class BookListResponse:
    result_type: str
    results: BookList
