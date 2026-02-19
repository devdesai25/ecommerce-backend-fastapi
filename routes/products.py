from fastapi import APIRouter, Depends
from services import product_service
from database import get_db
from models.products import product
router = APIRouter(
    tags=["product"]
)

@router.get("/products")
def products(products = product ,db: get_db = Depends()):
    return products