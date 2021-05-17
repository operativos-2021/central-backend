import scrapy
import json
import time


class MetacriticItem(scrapy.Item):
    productTitle = scrapy.Field()
    productMetascore = scrapy.Field()
    productUserScore = scrapy.Field()
    ProductPlatform = scrapy.Field()
    url = scrapy.Field()

class MetacriticspiderSpider(scrapy.Spider):
    name = 'metacriticspider'
    allowed_domain = ["https://www.metacritic.com"]
    myBaseUrl = ''
    start_urls = [1]
    
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls[0] =(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'scraping/outputfile_metacritic.json', 'CLOSESPIDER_TIMEOUT' : 15}


    def parse(self, response):
        items = MetacriticItem()
        title = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/a/h1/text()').get()
        metascore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/a/div/span/text()').get() 
        userscore = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div/text()').get()

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