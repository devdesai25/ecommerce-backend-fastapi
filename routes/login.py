from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.userRes import UserResponse
from services import login_service
from schemas.login_signup import userlogin
from database import get_db
router = APIRouter(
    tags=["Auth"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):

    return login_service.login(form_data,db)