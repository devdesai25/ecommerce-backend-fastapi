from fastapi import APIRouter
from services import product_service

router = APIRouter(
    tags=["Products"]
)

@router.get("/")
def products():
    return {"message" : "This is home page"}