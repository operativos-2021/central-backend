import json
import os

def doProcess():
    actual_path = os.path.dirname(os.path.abspath(__file__))
    result_path = actual_path + "\\scrape_result.json"
    file = open(result_path)
    data = json.load(file)
    return data