from fastapi import APIRouter,Depends
from services.protected_service import get_current_user
router = APIRouter(
    tags=["mepage"]
)

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user