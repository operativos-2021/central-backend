from flask_restful import  Resource
from scraping.webscraper import doScraping
from load_balance.proccess import getGamesFromBackend

import multiprocessing
import os
import json

final_data = {}
actual_path = os.path.dirname(os.path.abspath(__file__))
games_path = actual_path + "/game_list.json"
scrape_result_path = actual_path + "/scrape_result.json"
outputfile_amazon = actual_path.replace("\controllers","/scraping/outputfile_amazon.json")
outputfile_howlongtobeat = actual_path.replace("\controllers","/scraping/outputfile_howlongtobeat.json")
outputfile_playstation = actual_path.replace("\controllers","/scraping/outputfile_playstation.json")
outputfile_metacritic = actual_path.replace("\controllers","/scraping/outputfile_metacritic.json")
class load_balance(Resource):

    def get(self,games_range):
        def getGames(key_from,key_to):
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
        
            game_list_path = actual_path.replace("controllers","scraping/game_list.json")
            with open(scrape_result_path, "w") as outfile: 
                json.dump({}, outfile)
            f = open(game_list_path)
            games_data = json.load(f)
            
            keys = list(games_data["data"].keys())
            pc_limit = 8
            original_key_to = key_to
            start_index = key_from
            end_index = key_from
            while True:
                if key_to-key_from<=pc_limit:
                    end_index = original_key_to
                    key_to = 0
                else:
                    end_index += pc_limit
                    key_to -= pc_limit
                keys_to_scrape = keys[start_index:end_index]
                # print("Scraping del " + str(start_index) + " hasta el " + str(end_index))
                a_pool = multiprocessing.Pool()
                pool_result = a_pool.map(doScraping,keys_to_scrape)
                for game,game_info in pool_result:
                    final_data[game]=game_info
                if(key_to==0):
                    break
                else:
                    start_index +=pc_limit
                    
            with open(scrape_result_path, "w") as outfile: 
                    json.dump(final_data, outfile)
            
        print("Balanceo de cargas, rango: " + str(games_range))
        actual_path = os.path.dirname(os.path.abspath(__file__))
        scrape_result_path = actual_path.replace("controllers","scraping/scrape_result.json")

        with open(scrape_result_path, "w") as outfile: 
                json.dump({}, outfile)

        game_range_list = games_range.split("::")
        if int(game_range_list[0])==0:
            print("Soy el BackendPrincipal")
            game_range_1 = "-1::" + str(int(game_range_list[1])//2)
            game_range_2 = str(int(game_range_list[1])//2) +"::" + game_range_list[1]
            a_pool = multiprocessing.Pool()
            a_pool.map(getGamesFromBackend,["http://localhost:5001/load_balance/"+game_range_1,"http://localhost:5002/load_balance/"+game_range_2])
        else:
            key_from = int(game_range_list[0])
            key_to = int(game_range_list[1])
            if(key_from==-1):
                key_from +=1
            getGames(key_from,key_to)

        
        file = open(scrape_result_path)
        data = json.load(file)
        return {"data":data}