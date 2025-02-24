from fastapi import APIRouter, Query
from app.services.rawg import get_rawg_data

router = APIRouter()

@router.get("/search")
def search_games(query: str = Query(..., min_length=1)):
    """ Busca juegos según el término ingresado por el usuario """
    params = {"search": query}
    data = get_rawg_data("games", params)
    return data.get("results", [])
