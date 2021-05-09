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

op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument('--disable-gpu')
op.add_argument('--no-sandbox')
op.binary_location = GOOGLE_CHROME_PATH

browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=op)

actual_path = os.path.dirname(os.path.abspath(__file__))
result_path = actual_path + "/game_list.json"
f = open(result_path)
games_data = json.load(f)

def scrapWebsite(page, link):
    # if page == "Amazon":
    #     return scrapAmazon(link)
    if page == "PlaystationStore":
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


def doScraping(game_index):
    keysList = list(games_data["data"].keys())
    game_name = keysList[game_index]
    games_info[game_name] = {}
    for page in games_data["data"][game_name]:
        link = games_data["data"][game_name][page]
        if not link == "None":
            games_info[game_name][page] = scrapWebsite(page, link) 
    f.close()

    driver.close()

    # games_info[game_index] = str(game_index)
    
    print(games_info)
    actual_path = os.path.dirname(os.path.abspath(__file__))
    result_path = actual_path + "/scrape_result.json"

    # with open(result_path, "w") as outfile: 
    #     json.dump(games_info, outfile)
    with open(result_path, "r+") as file:
        data = json.load(file)
        data.update(games_info)
        file.seek(0)
        json.dump(data, file)
        
    file = open(result_path)
    data = json.load(file)
    return data