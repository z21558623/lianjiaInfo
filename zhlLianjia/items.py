# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TowninfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()  
    city = scrapy.Field()
    
    district = scrapy.Field()
    
    town = scrapy.Field()

    url = scrapy.Field()
    
    pass



class TradeinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()  
    listed_price = scrapy.Field()
    
    transaction_price = scrapy.Field()
    
    town = scrapy.Field()

    url = scrapy.Field()
    
    pass
