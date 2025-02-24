from firebase_admin import auth

def verify_token(id_token):
    """Verifica el token de Firebase Authentication."""
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception:
        return None
