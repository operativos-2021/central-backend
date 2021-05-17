from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from scraping.webscraper import doScraping

import multiprocessing
import os
import json
import scraping.webscraper as webscraper

actual_path = os.path.dirname(os.path.abspath(__file__))
games_path = actual_path + "/game_list.json"
scrape_result_path = actual_path + "/scrape_result.json"
outputfile_amazon = actual_path.replace("\controllers","/scraping/outputfile_amazon.json")
outputfile_howlongtobeat = actual_path.replace("\controllers","/scraping/outputfile_howlongtobeat.json")
outputfile_playstation = actual_path.replace("\controllers","/scraping/outputfile_playstation.json")
outputfile_metacritic = actual_path.replace("\controllers","/scraping/outputfile_metacritic.json")
final_data = {}
class games(Resource):
    def get(self, quantity):
        print(outputfile_amazon)
        if  os.path.exists(outputfile_amazon):
            os.remove(outputfile_amazon)
        if os.path.exists(outputfile_playstation):
            os.remove(outputfile_playstation)
        if os.path.exists(outputfile_metacritic):
            os.remove(outputfile_metacritic)
        if os.path.exists(outputfile_howlongtobeat):
            os.remove(outputfile_howlongtobeat)
        global final_data
        final_data = {}
        print("Obtener juegos: " + str(quantity))
        actual_path = os.path.dirname(os.path.abspath(__file__))
        scrape_result_path = actual_path.replace("controllers","scraping/scrape_result.json")
        game_list_path = actual_path.replace("controllers","scraping/game_list.json")
        with open(scrape_result_path, "w") as outfile: 
            json.dump({}, outfile)
    
        f = open(game_list_path)
        games_data = json.load(f)
        index = 0
        keys = list(games_data["data"].keys())
        pc_limit = 30
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
            pool_result = a_pool.map(doScraping,keys_to_scrape)
            for game,game_info in pool_result:
                final_data[game]=game_info

            if(quantity==0):
                break
            else:
                start_index +=pc_limit
        return {"data":final_data}


