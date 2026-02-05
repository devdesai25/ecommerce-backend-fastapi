from fastapi import FastAPI
from services import login_service
router = FastAPI()

router.post("/login")
def login(username: str, password:str):
    return login_service.login(username, password)