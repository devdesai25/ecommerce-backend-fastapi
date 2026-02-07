from fastapi import APIRouter
from schemas.login_signup import usersignup
from services.signup_service import signup_serv

router = APIRouter(
    tags=["signup"]
)

@router.post("/signup")
def signup(user:usersignup):
    
    return signup_serv(user) 