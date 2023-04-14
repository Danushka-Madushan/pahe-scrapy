from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from core.pahe import AnimePahe
from core.config import CORS

# API Endpoints
api = FastAPI()

api.add_middleware( CORSMiddleware,
    allow_origins = CORS,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@api.get("/search/{query}")
async def read_item(query: str) -> dict:
    return AnimePahe.getAnimeList(query)

@api.get("/session/{session}")
async def getEpisodes(session: str) -> dict:
    return AnimePahe.getEpisodes(session)

# UI Endpoints
app = FastAPI()

app.mount("/api", api)
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")
