import os
import requests
import json
import os

actual_path = os.path.dirname(os.path.abspath(__file__))

scrape_result_path = actual_path.replace("load_balance","scraping/scrape_result.json")

def getGamesFromBackend(url):
    response = requests.request("GET", url)
    data = json.loads(response.text)
    print(data["data"])
    with open(scrape_result_path, "r+") as file:
        data = json.load(file)
        data.update({data["data"]})
        file.seek(0)
        json.dump(data, file)