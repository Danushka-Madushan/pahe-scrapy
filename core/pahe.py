# All Functions Goes Here
import requests
from systems import getHeaders, ENV

class AnimePahe:
    def __init__(self) -> None:
        pass

    def getAnimeList(query: str) -> str:
        params = { 'm': 'search', 'q': query }
        response = requests.get(ENV.API, params=params, headers=getHeaders())
        return { "status": response.status_code, "content": response.json()}
