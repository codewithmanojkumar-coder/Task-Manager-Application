
from fastapi import FastAPI

from .database import engine, Base
from . import models
from .routers import tasks


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title="Task Manager API",
    description="A simple Task Manager Backend API",
    version="1.0.0"
)


# Connect task routes
app.include_router(tasks.router)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Task Manager API",
        "status": "Application is running"
    }
