from auth.jwt import decode, oauth2scheme
from fastapi import Depends, HTTPException
from database import get_db
from models.users import User
from schemas.login_signup import userlogin

def get_current_user(token = Depends(oauth2scheme), db = Depends(get_db)):
    payload = decode(token)
    if not payload:
        raise HTTPException(401,detail="Token Invalid")
    
    user_id = payload.get('sub')
    
    user = db.query(User).filter(User.id == user_id).first()
    
    return user