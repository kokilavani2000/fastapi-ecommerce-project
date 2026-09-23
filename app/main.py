from fastapi import FastAPI
from app.database.base import Base
from app.database.session import engine
from app.api.router import api_router

app = FastAPI(
    title="my first e-commerce project API",
    description="This is a simple e-commerce project API built with FastAPI",
    version="1.0.0",
)


Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to my first e-commerce project API!"
    }

app.include_router(api_router, prefix="/api/v1")