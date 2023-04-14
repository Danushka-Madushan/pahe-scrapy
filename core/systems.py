import json
import os

rel_path = lambda: os.path.dirname(os.path.relpath(__file__)) + '/'

class ENV:
    def __init__(self) -> None:
        pass

    API = 'https://animepahe.com/api'

def getHeaders() -> str:
    with open(rel_path() + 'headers.json', 'r') as headers:
        return json.load(headers)
