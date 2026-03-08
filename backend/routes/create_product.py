from fastapi import APIRouter, Depends
from services.product_service import productadd

router = APIRouter(
    prefix="/admin",
    tags=["Create"]
)

@router.post("/create")
def create_product(product : productadd = Depends()):
    print("Success")
    return product