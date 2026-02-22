from fastapi import APIRouter, Depends
from services.auth import get_current_user
router = APIRouter( 
    tags=["admin"]
)

@router.post("/admin")
def admin(current_user : get_current_user = Depends()):
    if current_user.get('role') != 'admin':
        return {"Access":"Denied"}
    
    return current_user