from fastapi import APIRouter, Depends, HTTPException
from services.auth import req_admin
from database import get_db
from schemas.product import ProductUpdate
from models.products import product 
router = APIRouter(
    prefix="/admin",
    tags=["Update"]
)

@router.patch("/products/{id}")
def update_product( cur_update : ProductUpdate, cur_product_id : int = id, admin: req_admin = Depends(), db : get_db = Depends()):
    
    db_product = db.query(product).filter(product.product_id == cur_product_id).first()
    
    if not db_product:
        raise HTTPException(404,detail="Product Not Found")

    db_product.name = cur_update.name 
    db_product.description = cur_update.description
    db_product.price = cur_update.price 
    db_product.stock = cur_update.stock

    db.commit()
    db.refresh(db_product)
    
    db_product = db.query(product).filter(product.product_id == cur_product_id).first()
    
    return db_product