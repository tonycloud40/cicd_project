from pathlib import Path

from fastapi import APIRouter

BASE_PATH = Path(__file__).resolve().parent.parent

api_router = APIRouter()


@api_router.get("/", status_code=200)
def src_basepath() -> dict:
    """
    Root show base path of the src folder
    """
    return {"basepath": BASE_PATH}


@api_router.get("/ping", status_code=200)
def src_ping() -> dict:
    """
    just an api test
    """
    return {"ping": "pong"}
