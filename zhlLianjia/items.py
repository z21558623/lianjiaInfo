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
    
    city = scrapy.Field()
    
    district = scrapy.Field()
    
    listed_date = scrapy.Field()
    
    listed_price = scrapy.Field()
    
    transaction_price = scrapy.Field()
#    成交周期
    transaction_cycle = scrapy.Field()
#    调价
    adjust_price = scrapy.Field()
#    带看
    house_inspection=scrapy.Field()
#    关注人士
    concerned_number =scrapy.Field()
#    浏览数
    browse_number =scrapy.Field()
#   户型结构
    house_type = scrapy.Field()
#    建筑面积
    covered_area=scrapy.Field()
#    朝向
    orientation = scrapy.Field()
#    配备电梯
    elevator = scrapy.Field()

#    成交信息
    transaction_info = scrapy.Field()
#   小区名
    cell_name = scrapy.Field()
#    所在楼层
    floors = scrapy.Field()
#    链接地址
    url = scrapy.Field()
    
    pass
