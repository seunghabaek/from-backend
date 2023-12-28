from typing import Optional
from pydantic import BaseModel

class ItemPayload(BaseModel):
    item_id: Optional[int]
    item_name: str
    quantity: int


# https://openapi.naver.com/v1/search/book.json?display=20&sort=sim&query=어
