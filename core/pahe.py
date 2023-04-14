# All Functions Goes Here
import requests
import re
from html import unescape
from .systems import getMaxRes, getHeaders, ENV

class AnimePahe:
    def __init__(self) -> None:
        pass

    def getAnimeList(query: str) -> dict:
        params = { 'm': 'search', 'q': query }
        response = requests.get(ENV.API, params=params, headers=getHeaders())
        return { "status": response.status_code, "content": response.json() if response.status_code == 200 else {} }

    def getEpisodes(session: str) -> dict:
        params = { 'm': 'release', 'id': session, 'sort': 'episode_asc', 'page': '1' }
        response = requests.get(ENV.API, params=params, headers=getHeaders())
        return { "status": response.status_code, "content": response.json() if response.status_code == 200 else {} }
    
    def getEpisode(session: str, playid: str) -> dict:
        response = requests.get(ENV.PLAY_API + session + '/' + playid)
        matches = re.findall(r'<a.href="(https?://pahe.win/[^"]+)".target="_blank"[^>]+.(.+?)<', response.content.decode('utf-8'))
        print(matches)
        if (len(matches) != 0):
            linkset = getMaxRes(matches)
            resp = requests.get(linkset[0])
            mat = re.findall(r',"(https?://kwik.cx/f/[^"]+)', resp.content.decode('utf-8'))
            return { "status": response.status_code, "content": { "link": mat[0], "info": unescape(linkset[1])} }
        else:
            return { "status": 500, "content": {} }
