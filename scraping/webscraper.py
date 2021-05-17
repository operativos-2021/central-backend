import crochet
crochet.setup()

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

import time
import os

output_data = []
crawl_runner = CrawlerRunner({
                'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.259'
            })


def doScraping(game):
    if os.path.exists('scraping/outputfile.json'):
        os.remove('scraping/outputfile.json')
    
    global baseURL

    baseAURL = 'https://www.amazon.com/-/es/dp/B010KYDNDG/ref=sr_1_3?__mk_es_US=ÅMÅŽÕÑ&dchild=1&keywords=Minecraft&qid=1619222234&sr=8-3'
    basePURL = 'https://store.playstation.com/en-us/product/UP4433-CUSA00744_00-MINECRAFTPS40001'
    baseNURL = 'https://store.nintendo.com/sushi-striker-the-way-of-sushido-nintendo-switch.html'
    baseMURL = 'https://www.metacritic.com/game/pc/minecraft'
    baseHURL = 'https://howlongtobeat.com/game?id=6064'

    scrape_with_crochet(baseURL=basePURL)
    
    return jsonify(output_data)  # Returns the scraped data after being running for 5 seconds.
    # os.system('cmd /c "cd '+actual_path+' && scrapy crawl hltbspider"')  

#@crochet.run_in_reactor
def scrape_with_crochet(baseURL):
    global crawl_runner

    # This will connect to the dispatcher that will kind of loop the code between these two functions.
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    
    # This will connect to the Spider function in our scrapy file and after each yield will pass to the crawler_result function.
    eventual = crawl_runner.crawl(PlaystationspiderSpider, category=baseURL)
    return eventual

def _crawler_result(item, response, spider):
    global output_data
    output_data.append(dict(item)) 