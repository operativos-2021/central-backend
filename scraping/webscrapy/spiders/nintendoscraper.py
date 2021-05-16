import scrapy
import json
import time


class NintendoItem(scrapy.Item):
    productTitle = scrapy.Field()
    productPrice = scrapy.Field()
    ProductSKU = scrapy.Field()
    url = scrapy.Field()

class NintendospiderSpider(scrapy.Spider):
    name = 'nintendospider'
    allowed_domain = ["store.nintendo.com"]
    myBaseUrl = ''
    start_urls = []
    
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'scraping/outputfile.json', 'CLOSESPIDER_TIMEOUT' : 15}

    def parse(self, response):
        items = NintendoItem()
        title = response.css('span.base::text').get()
        price = response.xpath('/html/body/div[2]/main/div[3]/div/div[1]/div[3]/div[1]/span/span/span[2]/span/text()').get() 
        print(title)

        items['productTitle'] = ''.join(title).strip()
        items['productPrice'] = ''.join(price).strip()
        items['productSKU'] = 'None'
        items['url'] = ''.join(response.url).strip()

        yield items