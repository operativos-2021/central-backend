from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from scraping.webscraper import doScraping
from scraping.webscraper import closeDriver
import multiprocessing
import os
import json
class games(Resource):
    def get(self,quantity):
        print("Obtener juegos: " + str(quantity))
        actual_path = os.path.dirname(os.path.abspath(__file__))
        scrape_result_path = actual_path.replace("controllers","scraping/scrape_result.json")
        game_list_path = actual_path.replace("controllers","scraping/game_list.json")

        with open(scrape_result_path, "w") as outfile: 
            json.dump({}, outfile)
    
        f = open(game_list_path)
        games_data = json.load(f)
        
        keys = list(games_data["data"].keys())
        pc_limit = 12
        start_index = 0
        end_index = 0
        while True:
            if quantity<=pc_limit:
                end_index += quantity
                quantity = 0
            else:
                end_index += pc_limit
                quantity -= pc_limit
            keys_to_scrape = keys[start_index:end_index]
            # print("Scraping del " + str(start_index) + " hasta el " + str(end_index))
            a_pool = multiprocessing.Pool()
            a_pool.map(doScraping,keys_to_scrape)
            if(quantity==0):
                break
            else:
                start_index +=pc_limit
        # doScraping(quantity)
        file = open(scrape_result_path)
        
        data = json.load(file)
        return {"data":data}


