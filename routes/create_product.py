from fastapi import APIRouter, Depends
from services.add_product import add

router = APIRouter(
    prefix="/admin",
    tags=["Create"]
)

@router.post("/product")
def create_product(product : add = Depends()):
    print("Success")
    return product