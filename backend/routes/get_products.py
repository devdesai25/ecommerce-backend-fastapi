from fastapi import APIRouter, Depends
from database import get_db
from models.products import product
from schemas.product import ProductResponse

router = APIRouter(
    tags=["product"]
)

@router.get("/products", response_model= list[ProductResponse])
def products(limit : int = 10, offset : int = 0,db: get_db = Depends()):
    
    all_prod = db.query(product).offset(offset).limit(limit).all()
    
    return all_prod