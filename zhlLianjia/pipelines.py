# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class ZhllianjiaPipeline(object):

    def open_spider(self, spider):
        self.result = pd.DataFrame(columns=['city','district','town', 'url'])

    
    def close_spider(self, spider):
        self.result.to_csv('towns.csv')
        print ("close")

    def process_item(self, item, spider):
        self.result = self.result.append(dict(item), ignore_index=True)
        return item
    
class TradeInfoPipeline(object):

    def open_spider(self, spider):
        self.result = pd.DataFrame(columns=['listed_price','transaction_price','town', 'url'])

    
    def close_spider(self, spider):
        self.result.to_csv('tradeinfo.csv')
        print ("close")

    def process_item(self, item, spider):
        self.result = self.result.append(dict(item), ignore_index=True)
        return item
    
