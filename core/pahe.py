# All Functions Goes Here
import requests
from .systems import getHeaders, ENV

class AnimePahe:
    def __init__(self) -> None:
        pass

    def getAnimeList(query: str) -> dict:
        params = { 'm': 'search', 'q': query }
        response = requests.get(ENV.API, params=params, headers=getHeaders())
        return { "status": response.status_code, "content": response.json() if response.status_code == 200 else {}}

    def getEpisodes(session: str) -> dict:
        params = { 'm': 'release', 'id': session, 'sort': 'episode_asc', 'page': '1' }
        response = requests.get('https://animepahe.com/api', params=params, headers=getHeaders())
        return { "status": response.status_code, "content": response.json() if response.status_code == 200 else {}}
