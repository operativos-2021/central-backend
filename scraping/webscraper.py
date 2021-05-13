from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import os

from scraping.scrapers.amazon_scraper import getAmazonInfo
from scraping.scrapers.playstation_scraper import getPlaystationInfo
from scraping.scrapers.nintendo_scraper import getNintendoInfo
from scraping.scrapers.metacritic_scraper import getMetacriticInfo
from scraping.scrapers.howlongtobeat_scraper import getHowLongToBeatInfo


global disable_continue
disable_continue = None

games_info = {}
actual_path = os.path.dirname(os.path.abspath(__file__))

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)


scrape_result_path = actual_path + "/scrape_result.json"
game_list_path = actual_path + "/game_list.json"

f = open(game_list_path)
games_data = json.load(f)

def scrapWebsite(page, link):
    if page == "Amazon":
        return scrapAmazon(link)
    elif page == "PlaystationStore":
        return scrapPlaystation(link)
    elif page == "NintendoStore":
        return scrapNintendo(link)
    elif page == "Metacritic":
        return scrapMetacritic(link)
    elif page == "HowLongToBeat":
        return scrapHLTB(link)
    
    
def scrapAmazon(url):
    global disable_continue

    if disable_continue == None:
        disable_continue = True
    else:
        disable_continue = False
    
    info = getAmazonInfo(driver, url, disable_continue)
    return info

def scrapPlaystation(url):
    info = getPlaystationInfo(driver, url)
    return info

def scrapNintendo(url):
    info = getNintendoInfo(driver, url)
    return info

def scrapMetacritic(url):
    info = getMetacriticInfo(driver, url)
    return info

def scrapHLTB(url):
    info = getHowLongToBeatInfo(driver, url)
    return info

def closeDriver():
    driver.close()
    
def doScraping(game):
    print(game)
    games_info[game] = {}
    for page in games_data["data"][game]:
        link = games_data["data"][game][page]
        if not link == "None":
            games_info[game][page] = scrapWebsite(page, link)
    with open(scrape_result_path, "r+") as file:
        data = json.load(file)
        data.update({game: games_info[game]})
        file.seek(0)
        json.dump(data, file)
    driver.close()
        
