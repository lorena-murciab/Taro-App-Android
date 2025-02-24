from fastapi import FastAPI
from app.routes import games, search, developers
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# from firebase_config import db

app = FastAPI()
# Incluir rutas
app.include_router(games.router, prefix="/games", tags=["Games"])
app.include_router(developers.router, prefix="/developers", tags=["Developers"])
app.include_router(search.router, prefix="/search", tags=["Search"])

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las fuentes, puedes restringirlo a dominios específicos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al backend!"}

# Ejecutamos el servidor en lugar de poner uvicorn main:app --reload
if __name__ == "__main__":
    try:
        uvicorn.run("app.__main__:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        print(e)

"""
@router.post("/add_user/")
def add_user(username: str, email: str):
    user_ref = db.collection("users").document()
    user_ref.set({
        "username": username,
        "email": email
    })
    return {"message": "Usuario agregado"}
"""
