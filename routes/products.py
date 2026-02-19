from fastapi import APIRouter, Depends
from services import product_service
from database import get_db
from models.products import product
from schemas.productres import productResponse
router = APIRouter(
    tags=["product"]
)

@router.get("/products", response_model= list[productResponse])
def products(db: get_db = Depends()):
    
    all_prod = db.query(product).all()

    return all_prod