from fastapi import APIRouter, Depends, HTTPException
from services.auth import req_admin
from database import get_db
from schemas.product import ProductUpdate
from models.products import product 
router = APIRouter(
    prefix="/admin",
    tags=["Update"]
)

@router.patch("/update/{id}")
def update_product( id : int ,cur_update : ProductUpdate, admin: req_admin = Depends(), db : get_db = Depends()):
    
    db_product = db.query(product).filter(product.product_id == id).first()
    
    if not db_product:
        raise HTTPException(404,detail="Product Not Found")

    update_data = cur_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_product,key,value)

    db.commit()
    db.refresh(db_product)
    
    return db_product