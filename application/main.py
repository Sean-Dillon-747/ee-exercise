from fastapi import FastAPI, HTTPException
from application.gists import fetch_user_gists

app = FastAPI(title="GitHub Gists API", version="1.0.0")

@app.get("/{username}")
def get_user_gists(username: str):
    try:
        return fetch_user_gists(username)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except RuntimeError as re:
        raise HTTPException(status_code=500, detail=str(re))