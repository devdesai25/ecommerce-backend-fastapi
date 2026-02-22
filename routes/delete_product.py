from fastapi import APIRouter, Depends, HTTPException
from services.auth import req_admin
from database import get_db
from models.products import product
router = APIRouter(
    prefix="/admin",
    tags=["delete"]
)

@router.delete("/prdouct/{id}")
def delete_prod(admin : req_admin = Depends(), db : get_db = Depends(),prod_id : int = id ):
    
    prod = db.query(product).filter(product.product_id == prod_id).first()

    if not product:
        raise HTTPException(404, detail="Product Not Found")
    
    db.delete(prod)
    db.commit()

    return {"200":"Product Delete Successfully"} 