from fastapi import APIRouter
from services import login_service
from schemas.login_signup import userlogin
router = APIRouter(
    tags=["Auth"]
)

@router.post("/login")
def login(user:userlogin):

    return login_service.login(user)