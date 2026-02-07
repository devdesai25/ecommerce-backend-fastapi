from fastapi import FastAPI
from config import settings
from database import engine, Base, metadata
from routes import login_router, product_router, signup_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login_router)
app.include_router(product_router)
app.include_router(signup_router)