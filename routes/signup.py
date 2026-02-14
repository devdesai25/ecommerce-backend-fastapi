from fastapi import APIRouter, Depends
from schemas.login_signup import usersignup
from services.signup_service import signup_serv
from database import get_db

router = APIRouter(
    tags=["signup"]
)

@router.post("/signup")
def signup(user:usersignup, db = Depends(get_db)):
    
    return signup_serv(user, db) 