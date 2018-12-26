# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from zhlLianjia.items import TradeinfoItem
import re
import json
import time
import random
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
        
    test = []
    def parse(self, response):
        print (response)
        page =  response.xpath('//div[@class="total fl"]/span/text()').extract_first() 
        page = int(int(page)/30+1)
        for i in range(1,page+1):
            url = response.url+'pg'+str(i)
            self.test.append(url)
            time.sleep(random.randint(5, 10)/100)
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
        tradeinfoItem['listed_date'] = response.xpath('//div[@class="transaction"]/div[2]/ul/li/text()').extract()[2].rstrip()
        
        tradeinfoItem['city'] = response.xpath('//div[@class="myAgent"]/div[1]/a/text()').extract()[0]
        tradeinfoItem['district'] = response.xpath('//div[@class="myAgent"]/div[1]/a/text()').extract()[1]
        
       
        for position in response.xpath('//div[@class="info fr"]'):
            tradeinfoItem['listed_price'] =  position.xpath('div[@class="msg"]/span/label/text()').extract()[0]       
            tradeinfoItem['transaction_cycle'] =  position.xpath('div[@class="msg"]/span/label/text()').extract()[1] 
            tradeinfoItem['adjust_price'] =  position.xpath('div[@class="msg"]/span/label/text()').extract()[2] 
            tradeinfoItem['house_inspection'] =  position.xpath('div[@class="msg"]/span/label/text()').extract()[3] 
            tradeinfoItem['concerned_number'] =  position.xpath('div[@class="msg"]/span/label/text()').extract()[4] 
            tradeinfoItem['browse_number'] =  position.xpath('div[@class="msg"]/span/label/text()').extract()[5] 
          
            tradeinfoItem['transaction_price'] =  position.xpath('div[@class="price"]/span/i/text()').extract_first()  
            tradeinfoItem['url'] = response.url
        
        
        tradeinfoItem['house_type'] = response.xpath('//div[@class = "base"]/div[@class="content"]/ul/li/text()').extract()[0].rstrip()
        tradeinfoItem['covered_area'] = response.xpath('//div[@class = "base"]/div[@class="content"]/ul/li/text()').extract()[2].rstrip()
        tradeinfoItem['orientation'] = response.xpath('//div[@class = "base"]/div[@class="content"]/ul/li/text()').extract()[6].rstrip()
        tradeinfoItem['elevator'] = response.xpath('//div[@class = "base"]/div[@class="content"]/ul/li/text()').extract()[13].rstrip()
       
        tradeinfoItem['floors'] = response.xpath('//div[@class = "base"]/div[@class="content"]/ul/li/text()').extract()[1].rstrip()


#        tradeinfoItem['cell_name'] = response.xpath('//*[@id="resblockCardContainer"]/div/div/div[1]/h3/span/text()').extract_first()
        tradeinfoItem['transaction_info'] = response.xpath('//div[@id="chengjiao_record"]/ul/li/p/text()').extract_first().rstrip()
        yield tradeinfoItem