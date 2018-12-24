# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from zhlLianjia.items import TowninfoItem
import re
import json

class LianjiachengjiaoSpider(scrapy.Spider):
    name = 'lianjiachengjiao'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://sh.lianjia.com/chengjiao']
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'zhlLianjia.pipelines.ZhllianjiaPipeline': 400
        }
    }
        
    
    def parse(self, response):
        print (response)
        for position in response.xpath('//div[@data-role="ershoufang"]/div/a'):
            towninfoItem = TowninfoItem()
            url =  position.xpath('@href').extract_first()  
            print ('zhltest')
            print (url)
            towninfoItem['city'] = 'sh'
            towninfoItem['district'] =  position.xpath('text()').extract_first() 
            url = 'https://sh.lianjia.com'+url
            yield scrapy.Request(url, callback=self.districtparse, meta={"towninfoItem": towninfoItem})
        
    
    def districtparse(self, response):
        print ("districtparse")
        towninfoItem = response.meta['towninfoItem']
        for position in response.xpath('//div[@data-role="ershoufang"]/div[2]/a'):
            towninfoItem['town'] =  position.xpath('text()').extract_first()            
            towninfoItem['url'] = 'https://sh.lianjia.com'+position.xpath('@href').extract_first()
            yield towninfoItem