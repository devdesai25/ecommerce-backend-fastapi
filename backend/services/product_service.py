from services.auth import req_admin
from fastapi import Depends, HTTPException
from schemas.product import ProductCreate
from database import get_db
from models.products import product
from models.users import User

def productadd(cur_product: ProductCreate, admin : req_admin = Depends(), db : get_db = Depends()):

    db_prod = db.query(product).filter(product.name == cur_product.name).first()
    
    if db_prod :
        raise HTTPException(409,detail="Duplicate Value inserted")

    add_prod = product(
        name = cur_product.name, 
        description = cur_product.description, 
        price = cur_product.price, 
        stock = cur_product.stock, 
        created_by = admin.id) 
    db.add(add_prod)
    db.commit()
    db.refresh(add_prod)
    return add_prod