import requests
from dotenv import load_dotenv
import os

load_dotenv()

RAWG_API_KEY = os.getenv("RAWG_API_KEY")
RAWG_BASE_URL = "https://api.rawg.io/api"

def get_rawg_data(endpoint, params={}):
    """ Función para hacer peticiones a la API de RAWG """
    url = f"{RAWG_BASE_URL}/{endpoint}"
    params["key"] = RAWG_API_KEY
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error en la solicitud a RAWG", "status_code": response.status_code}
