import os
import requests
import json
import os

actual_path = os.path.dirname(os.path.abspath(__file__))

scrape_result_path = actual_path.replace("load_balance","scraping/scrape_result.json")

def getGamesFromBackend(url):
    response = requests.request("GET", url)
    body = json.loads(response.text)
    print(body)
    print(body["data"])
    with open(scrape_result_path, "r+") as file:
        data = json.load(file)
        data.update(body["data"])
        file.seek(0)
        json.dump(data, file)