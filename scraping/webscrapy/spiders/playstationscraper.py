import scrapy
import json
import time


class PlaystationItem(scrapy.Item):
    productTitle = scrapy.Field()
    productPrice = scrapy.Field()
    ProductPlatform = scrapy.Field()
    url = scrapy.Field()

class PlaystationspiderSpider(scrapy.Spider):
    count = 0

    name = 'playstationspider'
    allowed_domain = ["https://store.playstation.com"]
    myBaseUrl = ''
    start_urls = []
    
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'scraping/outputfile.json', 'CLOSESPIDER_TIMEOUT' : 15}

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

        self.count += 1
        yield items