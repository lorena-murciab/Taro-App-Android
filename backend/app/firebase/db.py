import requests
from datetime import datetime, timedelta
from .config_db import db
from dotenv import load_dotenv
import os

load_dotenv()

RAWG_API_KEY = os.getenv("RAWG_API_KEY")

def fetch_rawg_data(endpoint):
    """Obtiene datos desde la API de RAWG"""
    url = f"https://api.rawg.io/api/{endpoint}?key={RAWG_API_KEY}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_last_update(collection_name):
    """Obtiene la última fecha de actualización de una colección"""
    doc_ref = db.collection("metadata").document(collection_name)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get("last_update")
    return None

def update_last_update(collection_name):
    """Actualiza la fecha de última modificación de una colección"""
    db.collection("metadata").document(collection_name).set({
        "last_update": datetime.utcnow().isoformat()
    })

def get_or_update_collection(collection_name, rawg_endpoint):
    """Consulta Firestore y actualiza los datos si es necesario"""
    last_update = get_last_update(collection_name)
    if last_update:
        last_update = datetime.fromisoformat(last_update)
        if datetime.utcnow() - last_update < timedelta(hours=24):
            # Si la última actualización fue hace menos de 24 horas, devolver los datos almacenados
            return [doc.to_dict() for doc in db.collection(collection_name).stream()]

    # Si no hay datos o están desactualizados, obtener nuevos de RAWG
    data = fetch_rawg_data(rawg_endpoint)
    if data:
        db.collection(collection_name).document("data").set({"items": data["results"]})
        update_last_update(collection_name)
    return data["results"] if data else []
