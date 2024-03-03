import json
import requests

from app.models import BookItem, BookList


def get_naver_books_list(query: str, display: int, sort: str, header_dict: dict):
    params = {'query': query, 'display': display, 'sort': sort}
    url = "https://openapi.naver.com/v1/search/book.json"

    response = requests.get(url=url, params=params, headers=header_dict)
    response_json = json.loads(response.content)

    return response_json


def get_book_list_response(response):

    items = response.get("items")

    items_list = [BookItem(
        title=item.get("title"),
        book_cover=item.get("image"),
        author=item.get("author"),
        publisher=item.get("publisher"),
        publish_date=item.get("pubdate"),
        isbn=item.get("isbn"),
        description=item.get("description"),
    ) for item in items
    ]

    book_list_response = BookList(
        total=response.get("total"),
        display=response.get("display"),
        items=items_list)

    return book_list_response
