from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.auth import get_current_user
from database import get_db
from models.users import User
from services.order_service import orderGet

router = APIRouter(
    tags=["GetOrders"]
    )

@router.get("/orders")
def get_order(
    user: User=Depends(get_current_user),
    db:Session=Depends(get_db)):
    
    return orderGet(user, db)