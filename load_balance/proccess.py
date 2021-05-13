import requests
import json

from time import time

def getGamesFromBackend(url):
    response = requests.request("GET", url)
    data = json.loads(response.text)
    print(data)