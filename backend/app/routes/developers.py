from fastapi import APIRouter
from app.services.rawg import get_rawg_data

router = APIRouter()

@router.get("/developers")
def get_developers():
    """ Obtiene una lista de desarrolladores de videojuegos """
    data = get_rawg_data("developers")
    return data.get("results", [])
