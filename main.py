from fastapi import FastAPI
from core.pahe import AnimePahe

app = FastAPI()

@app.get("/search/{query}")
async def read_item(query: str) -> dict:
    return AnimePahe.getAnimeList(query)
