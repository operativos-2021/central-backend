import crochet
import time
import os
import json
import random
# Importing our Scraping Function from the scrapers file
from scraping.webscrapy.spiders.amazonscraper import AmazonspiderSpider
from scraping.webscrapy.spiders.playstationscraper import PlaystationspiderSpider
from scraping.webscrapy.spiders.nintendoscraper import NintendospiderSpider
from scraping.webscrapy.spiders.metacriticscraper import MetacriticspiderSpider
from scraping.webscrapy.spiders.howlongtobeatscraper import HowLongToBeatspiderSpider
from flask import Flask , render_template, jsonify, request, redirect, url_for
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

final_data = {}
crochet.setup()
output_data = []
crawl_runner = CrawlerRunner({
                'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.259'
            })



actual_path = os.path.dirname(os.path.abspath(__file__))
games_path = actual_path + "/game_list.json"
scrape_result_path = actual_path + "/scrape_result.json"
outputfile_amazon = actual_path + "/outputfile_amazon.json"
outputfile_howlongtobeat = actual_path + "/outputfile_howlongtobeat.json"
outputfile_playstation = actual_path + "/outputfile_playstation.json"
outputfile_metacritic = actual_path + "/outputfile_metacritic.json"

f = open(games_path)
games_data = json.load(f)

def doScraping(game):
    print(game)
    global baseURL
    if  os.path.exists(outputfile_amazon):
        os.remove(outputfile_amazon)
    if os.path.exists(outputfile_playstation):
        os.remove(outputfile_playstation)
    if os.path.exists(outputfile_metacritic):
        os.remove(outputfile_metacritic)
    if os.path.exists(outputfile_howlongtobeat):
        os.remove(outputfile_howlongtobeat)

    baseAURL = games_data["data"][game]["Amazon"]
    basePURL = games_data["data"][game]["PlaystationStore"]
    baseMURL = games_data["data"][game]["Metacritic"]
    baseHURL = games_data["data"][game]["HowLongToBeat"]

    scrape_with_crochet_Amazon(baseURL=baseAURL)
    scrape_with_crochet_PlayStation(baseURL=basePURL)
    scrape_with_crochet_Metacritic(baseURL=baseMURL)
    scrape_with_crochet_HowLongToBeat(baseURL=baseHURL)
    games_final_result = collect_game_info()
    print(output_data)
    return game, games_final_result

def collect_game_info():
    time.sleep(2)
    game_info = {}
    for page in output_data:
        if page["url"].find("https://www.metacritic.com")!=-1:
            game_info["Metacritic"] = page
        elif page["url"].find("https://store.playstation.com")!=-1:
            game_info["PlaystationStore"] = page
        elif page["url"].find("https://howlongtobeat.com")!=-1:
            game_info["HowLongToBeat"] = page
        elif page["url"].find("https://www.amazon.com")!=-1:
            game_info["Amazon"] = page
    return game_info
#@crochet.run_in_reactor
def scrape_with_crochet_Amazon(baseURL):
    global crawl_runner
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(AmazonspiderSpider, category=baseURL)
    return eventual

def scrape_with_crochet_PlayStation(baseURL):
    global crawl_runner
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(PlaystationspiderSpider, category=baseURL)
    return eventual
    
def scrape_with_crochet_Metacritic(baseURL):
    global crawl_runner
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(MetacriticspiderSpider, category=baseURL)
    return eventual
      
def scrape_with_crochet_HowLongToBeat(baseURL):
    global crawl_runner
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(HowLongToBeatspiderSpider, category=baseURL)

    return eventual  

def _crawler_result(item, response, spider):
    global output_data
    output_data.append(dict(item)) 