from typing import List
from dataclasses import dataclass


# Book Search
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


# Book Review
@dataclass
class BookReview:
    reviewer: str
    review_preview: str


@dataclass
class BookDetail:
    title: str
    book_cover: str
    author: str
    publisher: str
    reviews: List[BookReview]
