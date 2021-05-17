import scrapy
import json
import time


class AmazonItem(scrapy.Item):
    productTitle = scrapy.Field()
    productPrice = scrapy.Field()
    ProductPlatform = scrapy.Field()
    url = scrapy.Field()

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    allowed_domain = ["amazon.com"]
    myBaseUrl = ''
    start_urls = [1]
   
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls[0] =(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'scraping/outputfile_amazon.json', 'CLOSESPIDER_TIMEOUT' : 15}

    def parse(self, response):
        items = AmazonItem()
        title = response.css('span.a-size-large.product-title-word-break::text').get()
        price = response.css('span.priceBlockBuyingPriceString::text').get()
        items['productTitle'] = ''.join(title).strip()
        items['productPrice'] = ''.join(price).strip()
        items['ProductPlatform'] = 'None'
        items['url'] = ''.join(response.url).strip()
        yield items