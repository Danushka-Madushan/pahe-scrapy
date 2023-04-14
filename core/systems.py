import json
import os
import re

rel_path = lambda: os.path.dirname(os.path.relpath(__file__)) + '/'

class ENV:
    def __init__(self) -> None:
        pass

    API = 'https://animepahe.com/api'
    PLAY_API = 'https://animepahe.com/play/'

def getHeaders() -> str:
    with open(rel_path() + 'headers.json', 'r') as headers:
        return json.load(headers)

def getMaxRes(links: list) -> list:
	data = {}
	sets = []

	for each in links:
		res = re.search(r'(?P<res>[0-9]{3,4})p', each[1])
		if (res.group('res') not in data):
			data[res.group('res')] = [each[0], each[1]]

	for x in data.keys():
		sets.append(int(x))

	return data[str(max(sets))]
