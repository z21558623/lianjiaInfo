# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from zhlLianjia.items import TradeinfoItem
import re
import json

class TradeInfoSpider(scrapy.Spider):
    name = 'tradeinfo'
    allowed_domains = ['lianjia.com']
    df = pd.read_csv('towns1.csv')
    start_urls = []
    for i in range(df.shape[0]):
        for j in range(1,8):            
            start_urls.append(df.iloc[i]['url']+'a'+str(j))
    custom_settings = {
        'ITEM_PIPELINES': {
            'zhlLianjia.pipelines.TradeInfoPipeline': 400
        }
    }
        
    
    def parse(self, response):
        print (response)
        page =  response.xpath('//div[@class="total fl"]/span/text()').extract_first() 
        page = int(int(page)/30+1)
        url = response.url+'pg'+str(page)
        yield scrapy.Request(url, callback=self.parse_bypage)
         
    def parse_bypage(self, response):    
        for position in response.xpath('//div[@class="info"]/div[@class="title"]/a'):
            
            url =  position.xpath('@href').extract_first()  
            tradeinfoItem = TradeinfoItem()
#            towninfoItem['city'] = 'sh'
#            towninfoItem['district'] =  position.xpath('text()').extract_first() 
#            url = 'https://sh.lianjia.com'+url
            yield scrapy.Request(url, callback=self.tradeinfoparse, meta={"tradeinfoItem": tradeinfoItem})
        
    
    def tradeinfoparse(self, response):
        print ("tradeinfoparse")
        tradeinfoItem = response.meta['tradeinfoItem']
        
        
       
        for position in response.xpath('//div[@class="info fr"]'):
            tradeinfoItem['listed_price'] =  position.xpath('div[@class="msg"]/span/label/text()').extract_first()       
            tradeinfoItem['transaction_price'] =  position.xpath('div[@class="price"]/span/i/text()').extract_first()  
            tradeinfoItem['url'] = response.url
        tradeinfoItem['town'] = response.xpath('//div[@id="chengjiao_record"]/ul/li/p/text()').extract_first()
        yield tradeinfoItem