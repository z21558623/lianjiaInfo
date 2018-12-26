# -*- coding: utf-8 -*-

import pandas as pd
from WindPy import *
import datetime,time
import os
 
class WindStock():
 
    def getCurrentTime(self):
        # 获取当前时间
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
    def AStockHisData(self,symbols,start_date,end_date,step=0):
        '''
        逐个股票代码查询行情数据
        wsd代码可以借助 WindNavigator自动生成copy即可使用;时间参数不设，默认取当前日期，可能是非交易日没数据;
        只有一个时间参数时，默认作为为起始时间，结束时间默认为当前日期；如设置两个时间参数则依次为起止时间
        '''
        print(self.getCurrentTime(),": Download A Stock Starting:")
        for symbol in symbols:
             w.start()
             try:
                 #stock=w.wsd(symbol,'trade_code,open,high,low,close,volume,amt',start_date,end_date)
                 '''
                 wsd代码可以借助 WindNavigator自动生成copy即可使用;
                 时间参数不设，默认取当前日期，可能是非交易日没数据;
                 只有一个时间参数，默认为起始时间到最新；如设置两个时间参数则依次为起止时间
                '''
                 stock=w.wsd(symbol, "trade_code,open,high,low,close,pre_close,volume,amt,dealnum,chg,pct_chg,vwap, adjfactor,close2,turn,free_turn,oi,oi_chg,pre_settle,settle,chg_settlement,pct_chg_settlement, lastradeday_s,last_trade_day,rel_ipo_chg,rel_ipo_pct_chg,susp_reason,close3, pe_ttm,val_pe_deducted_ttm,pe_lyr,pb_lf,ps_ttm,ps_lyr,dividendyield2,ev,mkt_cap_ard,pb_mrq,pcf_ocf_ttm,pcf_ncf_ttm,pcf_ocflyr,pcf_nflyr,trade_status", start_date,end_date)
                 index_data = pd.DataFrame()
                 index_data['trade_date']=stock.Times
                 stock.Data[0]=symbol
                 index_data['stock_code']=stock.Data[0]
                 #index_data['stock_code'] =symbol
                 index_data['open'] =stock.Data[1]
                 index_data['high'] =stock.Data[2]
                 index_data['low']  =stock.Data[3]
                 index_data['close']=stock.Data[4]
                 index_data['pre_close']=stock.Data[5]
                 index_data['volume']=stock.Data[6]
                 index_data['amt']=stock.Data[7]
                 index_data['dealnum']=stock.Data[8]
                 index_data['chg']=stock.Data[9]
                 index_data['pct_chg']=stock.Data[10]
                 #index_data['pct_chg']=index_data['pct_chg']/100
                 index_data['vwap']=stock.Data[11]
                 index_data['adj_factor']=stock.Data[12]
                 index_data['close2']=stock.Data[13]
                 index_data['turn']=stock.Data[14]
                 index_data['free_turn']=stock.Data[15]
                 index_data['oi']=stock.Data[16]
                 index_data['oi_chg']=stock.Data[17]
                 index_data['pre_settle']=stock.Data[18]
                 index_data['settle']=stock.Data[19]
                 index_data['chg_settlement']=stock.Data[20]
                 index_data['pct_chg_settlement']=stock.Data[21]
                 index_data['lastradeday_s']=stock.Data[22]
                 index_data['last_trade_day']=stock.Data[23]
                 index_data['rel_ipo_chg']=stock.Data[24]
                 index_data['rel_ipo_pct_chg']=stock.Data[25]
                 index_data['susp_reason']=stock.Data[26]
                 index_data['close3']=stock.Data[27]
                 index_data['pe_ttm']=stock.Data[28]
                 index_data['val_pe_deducted_ttm']=stock.Data[29]
                 index_data['pe_lyr']=stock.Data[30]
                 index_data['pb_lf']=stock.Data[31]
                 index_data['ps_ttm']=stock.Data[32]
                 index_data['ps_lyr']=stock.Data[33]
                 index_data['dividendyield2']=stock.Data[34]
                 index_data['ev']=stock.Data[35]
                 index_data['mkt_cap_ard']=stock.Data[36]
                 index_data['pb_mrq']=stock.Data[37]
                 index_data['pcf_ocf_ttm']=stock.Data[38]
                 index_data['pcf_ncf_ttm']=stock.Data[39]
                 index_data['pcf_ocflyr']=stock.Data[40]
                 index_data['pcf_ncflyr']=stock.Data[41]
                 index_data['trade_status']=stock.Data[42]
                 index_data['data_source']='Wind'
                 index_data['created_date']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                 index_data['updated_date']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                 index_data = index_data[index_data['open'] > 0]
                 #index_data.fillna(0)
                 try:
                    index_data.to_csv('stock_daily_data',mode='a',header ='false');
                 except Exception as e:
                     #如果写入数据库失败，写入日志表，便于后续分析处理
                     error_log=pd.DataFrame()
                     error_log['trade_date']=stock.Times
                     error_log['stock_code']=stock.Data[0]
                     error_log['start_date']=start_date
                     error_log['end_date']=end_date
                     error_log['status']=None
                     error_log['table']='stock_daily_data'
                     error_log['args']='Symbol: '+symbol+' From '+start_date+' To '+end_date
                     error_log['error_info']=e
                     error_log['created_date']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                     error_log.to_csv('stock_error_log')
                     print ( self.getCurrentTime(),": SQL Exception :%s" % (e) )
                     continue
                 w.start()
             except Exception as e:
                     #如果读取处理失败，可能是网络中断、频繁访问被限、历史数据缺失等原因。写入相关信息到日志表，便于后续补充处理
                     error_log=pd.DataFrame()
                     error_log['trade_date']=stock.Times
                     error_log['stock_code']=stock.Data[0]
                     error_log['start_date']=start_date
                     error_log['end_date']=end_date
                     error_log['status']=None
                     error_log['table']='stock_daily_data'
                     error_log['args']='Symbol: '+symbol+' From '+start_date+' To '+end_date
                     error_log['error_info']=e
                     error_log['created_date']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                     error_log.to_csv('stock_error_log')
                     print ( self.getCurrentTime(),":index_data %s : Exception :%s" % (symbol,e) )
                     time.sleep(sleep_time)
                     w.start()
                     continue
             print(self.getCurrentTime(),": Downloading [",symbol,"] From "+start_date+" to "+end_date)
        print(self.getCurrentTime(),": Download A Stock Has Finished .")
        

def main():
     global sleep_time,symbols
     sleep_time=5
     windStock=WindStock()
       
    
     start_date='20120101'
     end_date='20181231'
     print (start_date,end_date,'Starting')
     symbols = ['399241.SZ']
     windStock.AStockHisData(symbols,start_date,end_date)
     print (start_date,end_date,'Finished')
if __name__ == "__main__":
    main()