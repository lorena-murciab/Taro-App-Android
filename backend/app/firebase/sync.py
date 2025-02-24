import requests
from app.firebase.config_db import db
from dotenv import load_dotenv
import os

# Obtenemos la API_KEY de un archivo .env
load_dotenv()

RAWG_API_KEY = os.getenv("RAWG_API_KEY")

def fetch_rawg_data(endpoint):
    """Obtiene datos desde RAWG API"""
    url = f"https://api.rawg.io/api/{endpoint}?key={RAWG_API_KEY}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def sync_categories():
    """Sincroniza categorías desde RAWG a Firestore"""
    data = fetch_rawg_data("genres")
    if data:
        for category in data["results"]:
            db.collection("categories").document(str(category["id"])).set({
                "name": category["name"], # Nombre de la categoría
                "slug": category["slug"] # Slug de la categoría
            })
    print("✅ Categorías sincronizadas")

# Ejecutar sincronización
if __name__ == "__main__":
    sync_categories()
