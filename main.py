from fastapi import FastAPI
from config import settings
from database import engine, Base, metadata
from routes import login_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login_router)