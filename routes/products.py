from fastapi import FastAPI
from services import product_service
router = FastAPI()

router.post("/products")
def products():

    return product_service