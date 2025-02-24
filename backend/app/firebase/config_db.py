import firebase_admin
import os
from firebase_admin import credentials, firestore, auth

cred_path = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")

# Comprobamos que exite el archivo de credenciales
try:
    cred = credentials.Certificate(cred_path)
except FileNotFoundError:
    print("No se encontró el archivo {cred_path}")
    exit()

# Inicializar Firebase solo si no está inicializado
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Conectar Firestore
db = firestore.client()
