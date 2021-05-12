from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from scraping.webscraper import doScraping
from scraping.webscraper import closeDriver
import multiprocessing
import os
import json

#example to commit variables
# person_post_args = reqparse.RequestParser()
# person_post_args.add_argument("quantity",type=int,help="quantity", required=True)
# person_post_args.add_argument("gender",type=str,help="person gender", required=True)

# persons = {"juana":{"age":19,"gender":"mujer"},"juan":{"age":20,"gender":"hombre"}}

class games(Resource):
    # def get(self,name):
    #     if name not in persons:
    #         abort(400,message="Person not exist")
    #     return {"data":persons[name]}
    # def post(self,name):

    #     args = person_post_args.parse_args()
    #     persons[name] = args
    #     return persons[name],201
    def get(self,quantity):
        print("Hola")
        actual_path = os.path.dirname(os.path.abspath(__file__))
        scrape_result_path = actual_path.replace("controllers","scraping/scrape_result.json")
        game_list_path = actual_path.replace("controllers","scraping/game_list.json")

        # with open(scrape_result_path, "w") as outfile: 
        #     json.dump({}, outfile)
    
        # f = open(game_list_path)
        # games_data = json.load(f)
        
        # keys = list(games_data["data"].keys())

        # keys_to_scrape = keys[0:quantity]
        # a_pool = multiprocessing.Pool()
        # a_pool.map(doScraping,keys_to_scrape)
        # doScraping(quantity)
        file = open(scrape_result_path)
        
        data = json.load(file)
        return {"data":data}