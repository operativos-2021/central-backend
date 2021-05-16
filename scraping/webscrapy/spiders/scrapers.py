import scrapy
import json
import time

global count

class AmazonItem(scrapy.Item):
    productTitle = scrapy.Field()
    productPrice = scrapy.Field()
    ProductPlatform = scrapy.Field()
    url = scrapy.Field()

class AmazonspiderSpider(scrapy.Spider):
    # f = open(game_list_path)
    # games_data = json.load(f)

    # amazon_urls = []

    # for game in games_data["data"]:
    #     for page in games_data["data"][game]:
    #         link = games_data["data"][game][page]
    #         if not link == "None" and page == "Amazon":
    #             amazon_urls.append(link)

    name = 'amazonspider'
    allowed_domain = ["amazon.com"]
    myBaseUrl = ''
    start_urls = []
    custom_settings = {'FEED_URI': 'outputfile.json', 'CLOSESPIDER_TIMEOUT' : 15}

    def __init__(self, url='', **kwargs): # The category variable will have the input URL.
        print("Hola mundo")
        self.myBaseUrl = url
        self.start_urls.append(self.myBaseUrl)
        super().__init__(**kwargs)

    def parse(self, response):
        items = AmazonItem()
        title = response.css('span.a-size-large.product-title-word-break::text').get()
        price = response.css('span.priceBlockBuyingPriceString::text').get()
        print(price)

        items['productTitle'] = ''.join(title).strip()
        items['productPrice'] = ''.join(price).strip()
        items['ProductPlatform'] = 'None'
        items['url'] = ''.join(response.url).strip()

        yield items
        time.sleep(2)

class PlaystationItem(scrapy.Item):
    productTitle = scrapy.Field()
    productPrice = scrapy.Field()
    ProductPlatform = scrapy.Field()
    url = scrapy.Field()

class PlaystationspiderSpider(scrapy.Spider):
    f = open("scraping/game_list.json")
    games_data = json.load(f)

    playstation_urls = []

    game_names = list(games_data["data"].keys())
    count = 0

    for game in games_data["data"]:
        for page in games_data["data"][game]:
            link = games_data["data"][game][page]
            if not link == "None" and page == "PlaystationStore":
                playstation_urls.append(link)

    name = 'playstationspider'
    allowed_domain = ["https://store.playstation.com"]
    start_urls = playstation_urls

    def parse(self, response):
        items = PlaystationItem()
        title = response.css('h1.psw-m-b-xs.psw-h1.psw-l-line-break-word::text').get()
        price = response.css('span.psw-h3::text').get()
        print(title)

        try:
            items['productTitle'] = ''.join(title).strip()
        except:
            items['productTitle'] = ''.join(self.game_names[self.count]).strip()

        items['productPrice'] = ''.join(price).strip()
        items['ProductPlatform'] = 'None'
        items['url'] = ''.join(response.url).strip()

        yield items

        time.sleep(2)
        self.count += 1

class NintendoItem(scrapy.Item):
    productTitle = scrapy.Field()
    productPrice = scrapy.Field()
    ProductSKU = scrapy.Field()
    url = scrapy.Field()

class NintendospiderSpider(scrapy.Spider):
    f = open("scraping/game_list.json")
    games_data = json.load(f)

    nintendo_urls = []

    for game in games_data["data"]:
        for page in games_data["data"][game]:
            link = games_data["data"][game][page]
            if not link == "None" and page == "NintendoStore":
                nintendo_urls.append(link)

    name = 'nintendospider'
    allowed_domain = ["https://store.nintendo.com"]
    start_urls = nintendo_urls

    def parse(self, response):
        items = NintendoItem()
        title = response.css('span.base::text').get()
        price = response.xpath('/html/body/div[2]/main/div[3]/div/div[1]/div[3]/div[1]/span/span/span[2]/span/text()').get() 
        print(title)
        print(price)

        items['productTitle'] = ''.join(title).strip()
        items['productPrice'] = ''.join(price).strip()
        items['productSKU'] = 'None'
        items['url'] = ''.join(response.url).strip()

        yield items

        time.sleep(2)

class MetacriticItem(scrapy.Item):
    productTitle = scrapy.Field()
    productMetascore = scrapy.Field()
    productUserScore = scrapy.Field()
    ProductPlatform = scrapy.Field()
    url = scrapy.Field()

class MetacriticspiderSpider(scrapy.Spider):
    f = open("scraping/game_list.json")
    games_data = json.load(f)

    metacritic_urls = []

    for game in games_data["data"]:
        for page in games_data["data"][game]:
            link = games_data["data"][game][page]
            if not link == "None" and page == "Metacritic":
                metacritic_urls.append(link)

    name = 'metacriticspider'
    allowed_domain = ["https://www.metacritic.com"]
    start_urls = metacritic_urls

    def parse(self, response):
        items = MetacriticItem()
        title = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/a/h1/text()').get()
        metascore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/a/div/span/text()').get() 
        userscore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div/text()').get()
        print(title)
        print(metascore)

        if title:
            items['productTitle'] = ''.join(title).strip()
        else:
            try:
                title = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/a/h1/text()').get()
                items['productTitle'] = ''.join(title).strip()
            except:
                title = 'None'
                items['productTitle'] = ''.join(title).strip()

        if metascore:
            items['productMetascore'] = ''.join(metascore).strip()
        else:
            try:
                metascore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div/div/a/div/span/text()').get()
                items['productMetascore'] = ''.join(metascore).strip()
            except:
                metascore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div[3]/div[1]/div/div/a/div/span/text()').get()
                items['productMetascore'] = ''.join(metascore).strip()

        if userscore:
            items['productUserScore'] = ''.join(userscore).strip()
        else:
            try:
                userscore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/a/div/text()').get()
                items['productUserScore'] = ''.join(userscore).strip()
            except:
                userscore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div[3]/div[2]/div/div/a/div/text()').get()
                items['productUserScore'] = ''.join(userscore).strip()

        items['url'] = ''.join(response.url).strip()
        items['ProductPlatform'] = 'None'

        yield items

        time.sleep(1)

class HowLongToBeatItem(scrapy.Item):
    productTitle = scrapy.Field()
    productInfo = scrapy.Field()
    productImg = scrapy.Field()
    ProductSoloTime = scrapy.Field()
    ProductCoopTime = scrapy.Field()
    ProductVsTime = scrapy.Field()
    ProductMainStoryTime = scrapy.Field()
    ProductMainExtrasTime = scrapy.Field()
    ProductCompletionist = scrapy.Field()
    ProductAllStylesTime = scrapy.Field()
    url = scrapy.Field()

class HowLongToBeatspiderSpider(scrapy.Spider):
    f = open("scraping/game_list.json")
    games_data = json.load(f)

    hltb_urls = []

    for game in games_data["data"]:
        for page in games_data["data"][game]:
            link = games_data["data"][game][page]
            if not link == "None" and page == "HowLongToBeat":
                hltb_urls.append(link)

    name = 'hltbspider'
    allowed_domain = ["https://howlongtobeat.com"]
    start_urls = hltb_urls

    def parse(self, response):
        items = HowLongToBeatItem()
        title = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/text()').get()
        img = 'https://howlongtobeat.com' + response.xpath('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/img').xpath('@src').get()
        info = self.getProductInfo(response)    
        times = self.getProductTimes(response)

        print(title)

        items['productTitle'] = ''.join(title).strip()
        items['productInfo'] = info
        items['productImg'] = ''.join(img).strip()
        items['url'] = ''.join(response.url).strip()
        items['ProductSoloTime'] = times['Single-Player']
        items['ProductCoopTime'] = times['Co-Op']
        items['ProductVsTime'] = times['Vs.']
        items['ProductMainStoryTime'] = times['Main Story']
        items['ProductMainExtrasTime'] = times['Main + Extras']
        items['ProductCompletionist'] = times['Completionist']
        items['ProductAllStylesTime'] = times['All Styles']

        yield items

    def getProductInfo(self, response):
        description = True
        info_results = {}

        for i, info in enumerate(response.css('div.profile_info')):
            if description:
                text = response.xpath('//*[@id="global_site"]/div[3]/div/div[2]/div[2]/div[2]/text()').get()
                rest = response.xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/span/text()').get()
                print(text)
                print(rest)
                if rest:
                    text += rest

                description = False
                info_results['description'] = text
            else:
                title = info.css('strong::text').get().strip()
                content = info.css('div.profile_info::text')[-1].get().strip()
                title = title.replace(':', '')

                info_results[title] = content

        return info_results

    def getProductTimes(self, response):
        results = {'Single-Player': 'None', 'Co-Op': 'None', 'Vs.': 'None', 'Main Story': 'None',
            'Main + Extras': 'None', 'Completionist': 'None', 'All Styles': 'None'}

        times = response.css('div.game_times').css('ul')
        time_titles = times.css('h5::text').getall()
        time_contents = times.css('div::text').getall()

        for i, time_title in enumerate(time_titles):
            results[time_title] = time_contents[i].strip()

        return results
