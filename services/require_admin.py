from fastapi import Depends, HTTPException
from database import get_db
from .protected_service import get_current_user

def req_admin(admin : get_current_user = Depends()):

    if not admin.role == 'admin':
        raise HTTPException(401, detail= " Unauthorized access")
    
    return admin