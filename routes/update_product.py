from fastapi import APIRouter, Depends, HTTPException
from services.auth import req_admin
from database import get_db
from schemas.product import ProductUpdate

router = APIRouter(
    prefix="/admin",
    tags=["Update"]
)

@router.patch("/products/{id}")
def update_prod( prod_upd = ProductUpdate, prod_id : int = id, admin: req_admin = Depends(), db : get_db = Depends()):
    return prod_upd