from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from scraping.webscraper import doScraping

import multiprocessing
import os
import json
import scraping.webscraper as webscraper

final_data = {}
class games(Resource):
    def get(self, quantity):
        global final_data
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
            #Save Data 
            # file = open(scrape_result_path)
            # data = json.load(file)
            # with open(scrape_result_path, "w") as outfile: 
            #     json.dump({}, outfile)
            # final_data[str(index)] = data

            if(quantity==0):
                break
            else:
                start_index +=pc_limit
            # index += 1
        # keys = list(games_data["data"].keys())
        # print("A iniciar: " + keys[0])
        # doScraping(keys[0])
        # print("A iniciar: " + keys[1])
        # doScraping(keys[1])
        # output = {}
        # for page in final_data:
        #     for game in page:
        #         output[game.key()]=final_data[page][game]
        return {"data":final_data}


