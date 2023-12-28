import json
import requests


def get_naver_books_list(query: str, display: int, sort: str, header_dict: dict):
    params = {'query': query, 'display': display, 'sort': sort}
    url = "https://openapi.naver.com/v1/search/book.json"

    response = requests.get(url=url, params=params, headers=header_dict)
    response_json = json.loads(response.content)

    return response_json
