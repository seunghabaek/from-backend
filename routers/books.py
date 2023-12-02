from fastapi import APIRouter, Depends

router = APIRouter(
	prefix="/books",
    tags=["books"],
    dependencies=[Depends()],
)

@router.get("/get_book_list")
def get_book_list() -> dict[str, str]:
    return {"message": "Hello World"}
    