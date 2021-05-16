from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import os

global disable_continue
disable_continue = None

games_info = {}
actual_path = os.path.dirname(os.path.abspath(__file__))


scrape_result_path = actual_path + "/scrape_result.json"
game_list_path = actual_path + "/game_list.json"


# def doScraping(game):
#     with open(scrape_result_path, "r+") as file:
#         data = json.load(file)
#         data.update({str(game): "mundo"})
#         file.seek(0)
#         json.dump(data, file)
        
import crochet
crochet.setup()

from scraping.webscrapy.spiders.scrapers import AmazonspiderSpider

from flask import Flask , render_template, jsonify, request, redirect, url_for
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time

# Importing our Scraping Function from the amazon_scraping file
output_data = []
crawl_runner = CrawlerRunner()

def _crawler_result(item, response, spider):
    output_data.append(dict(item)) 

def scrape_with_crochet(baseURL):
    baseURL = baseURL
    # This will connect to the dispatcher that will kind of loop the code between these two functions.
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    
    # This will connect to the ReviewspiderSpider function in our scrapy file and after each yield will pass to the crawler_result function.
    eventual = crawl_runner.crawl(AmazonspiderSpider, url = baseURL)
    return eventual

def doScraping(game):
    with open(scrape_result_path, "r+") as file:
        data = json.load(file)
        data.update({str(game): "mundo"})
        file.seek(0)
        json.dump(data, file)
    global baseURL
    baseURL = 'https://www.amazon.com/-/es/Animal-Crossing-New-Horizons/dp/B07SV4WDHK/ref=sr_1_4?__mk_es_US=ÅMÅŽÕÑ&dchild=1&keywords=Animal+Crossing&qid=1619285077&sr=8-4'
    scrape_with_crochet(baseURL = baseURL)
    print(output_data)
    
    return jsonify(output_data) # Returns the scraped data after being running for 20 seconds.
    # os.system('cmd /c "cd '+actual_path+' && scrapy crawl hltbspider"')  