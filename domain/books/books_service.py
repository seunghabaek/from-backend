import requests

def get_naver_books_list(query: str, display: int, sort="sim"):
    params = {'query': {query}, 'display': {display}, 'sort': {sort}}
    url = "https://openapi.naver.com/v1/search/book.json"
    response = requests.get(url, params=params)
    return response
