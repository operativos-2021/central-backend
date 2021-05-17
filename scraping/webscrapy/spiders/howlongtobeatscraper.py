import scrapy
import json
import time


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
    name = 'hltbspider'
    allowed_domain = ["https://howlongtobeat.com"]
    myBaseUrl = ''
    start_urls = [1]
    
    def __init__(self, category='', **kwargs): # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls[0] =(self.myBaseUrl)
        super().__init__(**kwargs)

    custom_settings = {'FEED_URI': 'scraping/outputfile_howlongtobeat.json', 'CLOSESPIDER_TIMEOUT' : 15}


    def parse(self, response):
        items = HowLongToBeatItem()
        title = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/text()').get()
        img = 'https://howlongtobeat.com' + response.xpath('/html/body/div[1]/div/div[3]/div/div[1]/div[1]/img').xpath('@src').get()
        info = self.getProductInfo(response)    
        times = self.getProductTimes(response)

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
