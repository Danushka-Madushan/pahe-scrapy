import json

class ENV:
    def __init__(self) -> None:
        pass

    API = 'https://animepahe.com/api'

def getHeaders() -> str:
    with open('headers.json', 'r') as headers:
        return json.load(headers)
