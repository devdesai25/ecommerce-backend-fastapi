from fastapi import APIRouter
from services import login_service
from schemas.login_signup import userlogin
router = APIRouter(
    tags=["Auth"]
)

@router.get("/login")
def login():
    return {"message" : "Received"}