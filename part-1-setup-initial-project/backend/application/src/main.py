from fastapi import FastAPI
import uvicorn

from src.router.routes import api_router

app = FastAPI()

app.include_router(api_router)

def start():
    """Launched with poetry run start' at root level"""
    uvicorn.run("src.main:app",
                host="127.0.0.1", 
                port=8000, 
                reload=True)