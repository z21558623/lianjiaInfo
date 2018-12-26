# -*- coding: utf-8 -*-

from os import walk
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
dataframe_list = []
old_str='\"\"'
new_str=''
#walk会返回3个参数，分别是路径，目录list，文件list，你可以按需修改下
df = pd.read_csv('tradeinfo.csv',delimiter=',',parse_dates=[3])
print (df)

dfs1=df.set_index(df['listed_date'])
dfs1.index.drop_duplicates()
pd.to_datetime(dfs1['listed_date'],errors='coerce')
dfs1['listed_date'].apply(str)
dfs1 = dfs1.sort_values(by=['listed_date'])
days = dfs1.ix[:,['transaction_info']]

days['unit_price'] = days['transaction_info'].str.extract('(\d+)', expand=False)
days1 = days.dropna(how='all')
days1['unit_price'] = days1['unit_price'].apply(int)

pd.to_datetime(days1.index,errors='coerce')
bars = days1.unit_price.resample('M').mean()
bars.plot()


stock = pd.read_csv('stock_daily_data')
stock['trade_date'] = pd.to_datetime(stock['trade_date'],errors='coerce')
stock = stock.sort_values(by=['trade_date'])
stock['pre_close'] = stock['pre_close'].apply(np.float)
stock1=stock.set_index(stock['trade_date']) 
stock1 = stock1.ix[:,['pre_close']]
stock1 = stock1.dropna(how='all')
stock1.plot()
stock1 = stock1.pre_close.resample('M').mean()
pearson_correlation = stock1.corr(bars)

#print (dataframe_list)
#dfs = pd.DataFrame(columns=dataframe_list[0].columns)
#for df in dataframe_list:
#    df = df
#    dfs = dfs.append(df)
#    
##dfs = dataframe_list[3]
#print (dfs)
#dfs1=dfs.set_index(dfs['date'])
#dfs1.index.drop_duplicates()
#pd.to_datetime(dfs1['date'],errors='coerce')
#dfs1['date'].apply(str)
##dfs1.sort_values(by=['date'])
#
#
#ticks = dfs1.ix[:,['score']]
#ticks1 = ticks.dropna(how='all')
#
#pd.to_datetime(ticks1.index,errors='coerce')
#bars = ticks1.score.resample('M').count()
#bars.plot()
#df.sort_values(by='date')ti
#df['date'].apply(pd.to_datetime,errors='ignore')
#bars = ticks1.score.resample('M').count()
#ticks1 = ticks.dropna(how='all')
#print (df)
#ticks = df1.ix[:,['score']]
#    
    
#    list = df['date'].head(10)