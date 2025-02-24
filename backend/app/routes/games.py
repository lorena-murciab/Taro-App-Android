from fastapi import APIRouter
from app.firebase.db import get_or_update_collection

router = APIRouter()

@router.get("/categories")
def get_categories():
    """Devuelve todas las categorías de videojuegos"""
    return {"categories": get_or_update_collection("categories", "genres")}

@router.get("/games")
def get_games():
    """Devuelve todos los juegos principales (sin DLCs ni expansiones)"""
    games = get_or_update_collection("games", "games")
    filtered_games = [game for game in games if not game.get("tags") or "DLC" not in game["tags"]]
    return {"games": filtered_games}

@router.get("/developers")
def get_developers():
    """Devuelve todas las empresas desarrolladoras de videojuegos"""
    return {"developers": get_or_update_collection("developers", "developers")}
