#!/usr/bin/env python
# coding: utf-8

# In[12]:


stalks = {}
def breakofStructure():
    
    flag = False
    stk_up = []
    stk_down = []
    for key in list(stalks):
        
        data = getStockData(key, "1d", '5m')
        refactorData(data)
        
        
        entry = stalks[key][0]
        stoploss = stalks[key][1]
        position = stalks[key][2]
        
        if "Long" in position:
            
            if(data["Low"][0] < stoploss):
                #remove item since it goes below stoploss
                del stalks[key]
                
            
            elif(data["High"][0] > data["High"][1]):
                #break high of previous candle
                
                #notify
                Strike_price, ent, SL = optionPremium(key,data["High"][1],entry-stoploss, "long")
                
                if(flag==False):
                
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    send_to_telegram("Time Now ======"  + dt_string)
                    flag = True
                    
                send_to_telegram(key+" " + str(Strike_price) + "CE \n" + "Entry : " + str(entry) + "\nStoploss : " + str(stoploss) + "\nPosition :" +position + "\nStrike Price :" +str(Strike_price) +" CE \n Entry :" +str(ent) + "\nStoploss :" +str(SL))
                stk_up.append(key.replace(".NS",""))
                
                del stalks[key]
                
                
        else:
            if(data["High"][0] > stoploss):
                #remove item since it goes below stoploss
                del stalks[key]
            
            elif(data["Low"][0] < data["Low"][1]):
                #break high of previous candle
                
                #notify
                Strike_price, ent, SL = optionPremium(key,data["Low"][1],entry-stoploss, "short")
                
                if(flag==False):
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    send_to_telegram("Time Now ======"  + dt_string)
                    flag = True
                send_to_telegram(key+" " + str(Strike_price) + "PE \n" + "Entry : " + str(entry) + "\nStoploss : " + str(stoploss) + "\nPosition :" +position + "\nStrike Price :" +str(Strike_price) +" PE \n Entry :" +str(ent) + "\nStoploss :" +str(SL))
                stk_down.append(key.replace(".NS",""))
                
          
                del stalks[key]
    print("Uptrend : ", stk_up)
    print("Downtrend : ", stk_down)
    tot=[]
    for i in stk_up:
        tot.append(i)
    for i in stk_down:
        tot.append(i)
    print("all stlk : ", tot)


# In[5]:


import talib as ta
import yfinance as yf
import pandas as pd
import numpy as np
import time

import requests
import schedule
from datetime import datetime

# print(fnolist())


# In[6]:


fno_list = [ 'ADANIENT', 'RAIN', 'HINDCOPPER', 'NATIONALUM', 'ABCAPITAL', 'BHEL', 'DELTACORP', 'JINDALSTEL', 'HAL', 'FEDERALBNK', 'VEDL', 'HINDALCO', 'PNB', 'AMBUJACEM', 'INDIACEM', 'IBULHSGFIN', 'RBLBANK', 'BANKBARODA', 'L&TFH', 'NMDC', 'SRF', 'CANBK', 'GNFC', 'CHAMBLFERT', 'AUBANK', 'SAIL', 'DEEPAKNTR', 'ABB', 'PFC', 'UPL', 'MANAPPURAM', 'JKCEMENT', 'BEL', 'ABFRL', 'SBIN', 'CUMMINSIND', 'RAMCOCEM', 'INDUSINDBK', 'AXISBANK', 'TECHM', 'PERSISTENT', 'TCS', 'SUNTV', 'IDEA', 'CUB', 'CROMPTON', 'LICHSGFIN', 'INDIAMART', 'HCLTECH', 'HONAUT', 'ACC', 'DALBHARAT', 'MCX', 'IDFC', 'TATACHEM', 'LTTS', 'AARTIIND', 'METROPOLIS', 'UBL', 'MOTHERSON', 'BANDHANBNK', 'COROMANDEL', 'IEX', 'SHRIRAMFIN', 'INTELLECT', 'NAVINFLUOR', 'ZEEL', 'ONGC', 'CONCOR', 'TATASTEEL', 'INDHOTEL', 'JSWSTEEL', 'GUJGASLTD', 'GODREJPROP', 'EXIDEIND', 'COALINDIA', 'HAVELLS', 'BALKRISIND', 'MPHASIS', 'ADANIPORTS', 'BOSCHLTD', 'MARUTI', 'M&MFIN', 'ZYDUSLIFE', 'GRANULES', 'BALRAMCHIN', 'PIIND', 'IOC', 'CHOLAFIN', 'TATAMOTORS', 'ATUL', 'BAJAJ-AUTO', 'GMRINFRA', 'ABBOTINDIA', 'WIPRO', 'TRENT', 'DIXON', 'EICHERMOT', 'DLF', 'PVR', 'GRASIM', 'BHARTIARTL', 'MGL', 'IDFCFIRSTB', 'ASTRAL', 'RELIANCE', 'KOTAKBANK', 'TATAPOWER', 'PEL', 'BHARATFORG', 'VOLTAS', 'MRF', 'TORNTPHARM', 'BAJAJFINSV', 'MARICO', 'BSOFT', 'DRREDDY', 'NAUKRI', 'NTPC', 'DIVISLAB', 'BAJFINANCE', 'COLPAL', 'HEROMOTOCO', 'FSL', 'SYNGENE', 'INFY', 'GAIL', 'POLYCAB', 'RECLTD', 'OBEROIRLTY', 'APOLLOTYRE', 'SIEMENS', 'ASIANPAINT', 'SHREECEM', 'TORNTPOWER', 'NESTLEIND', 'ITC', 'JUBLFOOD', 'LUPIN', 'LT', 'TITAN', 'MCDOWELL-N', 'M&M', 'HDFC', 'LTIM', 'MFSL', 'SUNPHARMA', 'AUROPHARMA', 'IRCTC', 'BERGEPAINT', 'CANFINHOME', 'WHIRLPOOL', 'PAGEIND', 'HDFCLIFE', 'TATACONSUM', 'SBICARD', 'ICICIBANK', 'HINDUNILVR', 'ULTRACEMCO', 'TATACOMM', 'ESCORTS', 'BATAINDIA', 'SBILIFE', 'APOLLOHOSP', 'COFORGE', 'HDFCAMC', 'PIDILITIND', 'LAURUSLABS', 'IGL', 'HINDPETRO', 'HDFCBANK', 'INDUSTOWER', 'ICICIGI', 'GLENMARK', 'IPCALAB', 'OFSS', 'BPCL', 'BIOCON', 'ICICIPRULI', 'PETRONET', 'CIPLA', 'DABUR', 'INDIGO', 'ASHOKLEY', 'LALPATHLAB', 'MUTHOOTFIN', 'GODREJCP', 'POWERGRID', 'ALKEM', 'BRITANNIA', 'TVSMOTOR']

def getStockData(stockName,per ="1mo", inter = '1h'):
    msft = yf.Ticker(stockName)
    # get historical market data
#     hist = msft.history(period="3mo",interval='1d',start='2022-11-01', end = "2023-01-20")
#1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    hist = msft.history(period=per,interval=inter) 
    data = pd.DataFrame(hist)
    return data

def refactorData(data):
#     data.drop(['Volume', 'Dividends','Stock Splits'], axis=1,inplace=True)
    data["swing_low"] = (data['Low'] < data['Low'].shift(1)) & (data['Low'] < data['Low'].shift(-1))
    data["swing_high"] = (data['High'] >data['High'].shift(1)) & (data['High'] >data['High'].shift(-1))
    data["atr"] = ta.ATR(data['High'], data['Low'], data['Close'],14)
    data.sort_index(axis=0,inplace=True,ascending= False)
    data.insert(0, 'index', range(0, 0 + len(data)))
    
def send_to_telegram(message):

    apiToken = '6144260796:AAFOsCVPDaWGxPDELNKVR_HFB6Xjq0xy6Fs'  #15 min
#     apiToken = '6269646123:AAEn3tf2NJGOY4_icQwQjWZ4jSQZsng9PSk'  # 1 hr
#     apiToken = '6105515639:AAHgv_BYVchJ6kk5-L_b8TT2730lORhSlzU'  # 4 h
#     apiToken = '5887318572:AAEdQjRDBCWcPLiHonGb5PRKmS6sqOhmoqo'  # daily
    chatID = '940377958'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)
        
def optionPremium(symbol,spot_entry,SL_points,position):
    sym = symbol.replace(".NS","").replace("&","%26");

    response = requests.get(f"https://h9cg992bof.execute-api.ap-south-1.amazonaws.com/webapi/option/fatch-option-chain?symbol={sym}&expiryDate=")
    dta = response.json()

    call_ind = -1
    put_ind = -1
    


    for i in range(0, len(dta["resultData"]['opDatas']),1):

        if( dta["resultData"]['opDatas'][i]['strike_price'] > spot_entry):
            call_ind = i
            put_ind = i-1
            break
            
    strike_prices=dta["resultData"]['opDatas']
    
    if(put_ind == -1):
        print(symbol,spot_entry,SL_points,position )
    if(position=="long"):
        Strike_price = strike_prices[call_ind]['strike_price']
        entry = strike_prices[call_ind]['calls_ltp']
        delta = strike_prices[call_ind]['call_delta']
        stoploss = entry - SL_points*delta
        
        return Strike_price, entry ,stoploss;
    
    Strike_price = strike_prices[put_ind]['strike_price']
    entry = strike_prices[put_ind]['puts_ltp']
    delta = strike_prices[put_ind]['put_delta']
    stoploss = entry - SL_points*delta

    return Strike_price, entry ,stoploss;





# In[22]:


def resistance(data,symbol):
    flag = False
    false_support = -1
    lookback= 20
    pivot_len = 1
    index_of_recent_pivot = -1
    
    
    
    #i is first pivot
    #j is second pivot
    for i in range(pivot_len+1, lookback, 1):
        
        # first pivot found
        if((data['swing_high'][i] == True) ):
            
            max_pivot = data["High"][i] + 0.1 * data["atr"][i]  # max
            min_pivot = data["High"][i] - 0.2 * data["atr"][i]
            
            if(data["High"][1] > max_pivot):
                return False , "","" ,"";
            
            if(((data["Close"][0] <= max_pivot) and (data["Close"][0] >= min_pivot)) and ((data["High"][0] <= max_pivot) and (data["High"][0] >= min_pivot))):

                return True , data["High"][i] , max_pivot, "Short " + "\u2764\ufe0f";
            return False , "","" ,"";
    return False , "","" ,"";


# In[23]:


def support(data,symbol):
    flag = False
    false_support = -1
    lookback= 20
    pivot_len = 1
    index_of_recent_pivot = -1
    
    
    
    #i is first pivot
    #j is second pivot
    for i in range(pivot_len+1, lookback, 1):
        
        # first pivot found
        if((data['swing_low'][i] == True) ):
            
            max_pivot = data["Low"][i] + 0.2 * data["atr"][i]  # max
            min_pivot = data["Low"][i] - 0.1 * data["atr"][i]
            if(data["Low"][1] < min_pivot) :
                return False , "","" ,"";

            if(((data["Close"][0] <= max_pivot) and (data["Close"][0] >= min_pivot)) and ((data["Low"][0] <= max_pivot) and (data["Low"][0] >= min_pivot))):
                
                return True , data["Low"][i] , min_pivot, "Long " + '\U0001F49A';
            return False , "","","" ;
    return False , "","" ,"";


# In[24]:


stalks = {}
def breakofStructure():
    
    flag = False
    stk_up = []
    stk_down = []
    for key in list(stalks):

        data = getStockData(key, "1d", '5m')
        refactorData(data)
        
        
        entry = stalks[key][0]
        stoploss = stalks[key][1]
        position = stalks[key][2]
        
        if "Long" in position:
            #go short breakout
            
            if(data["Close"][1] < stoploss):
                print("short it" , key)
                #remove item since it goes below stoploss
                Strike_price, ent, SL = optionPremium(key,data["Close"][1],data["High"][1] - data["Close"][1], "short")
                
                if(flag==False):
                
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    send_to_telegram("Time Now ======"  + dt_string)
                    flag = True
                    
                send_to_telegram(key+" " + str(Strike_price) + "PE \n" + "Entry : " + str(entry) + "\nStoploss : " + str(stoploss) + "\nPosition :" +position + "\nStrike Price :" +str(Strike_price) +" PE \n Entry :" +str(ent) + "\nStoploss :" +str(SL))
                stk_down.append(key.replace(".NS",""))
                
                del stalks[key]
                
                
        else:
            if(data["Close"][1] > stoploss):
                print("Long it" , key)
                Strike_price, ent, SL = optionPremium(key,data["Close"][1],data["Close"][1] - data["Low"][1] , "Long")
                
                if(flag==False):
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    send_to_telegram("Time Now ======"  + dt_string)
                    flag = True
                send_to_telegram(key+" " + str(Strike_price) + "PE \n" + "Entry : " + str(entry) + "\nStoploss : " + str(stoploss) + "\nPosition :" +position + "\nStrike Price :" +str(Strike_price) +" CE \n Entry :" +str(ent) + "\nStoploss :" +str(SL))
                stk_up.append(key.replace(".NS",""))
                
          
                del stalks[key]
    print("Uptrend : ", stk_up)
    print("Downtrend : ", stk_down)
    tot=[]
    for i in stk_up:
        tot.append(i)
    for i in stk_down:
        tot.append(i)
    print("all stlk : ", tot)
    

                


# In[25]:


def dataProcessing():
    for sym in fno_list:
        symbol = sym  + ".NS"
        #symbol not in present in both maps then only start searching for new stalk 
        if symbol not in stalks :
                
            data = getStockData(symbol)
            refactorData(data)
            isuptrend,entry, stoploss,position= support(data,symbol)
            if(isuptrend):
                stalks[symbol] = [entry, stoploss,position]
            isdowntrend,entry, stoploss,position= resistance(data,symbol)
            if(isdowntrend):
                stalks[symbol] = [entry, stoploss,position]
    breakofStructure()


# In[26]:


import time
import requests
import schedule
      
def mainJob():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("starting at ", current_time)
    dataProcessing() 

#starting timing    
schedule.every(1).minutes.do(mainJob).until("15:30:15")

while(True):
    schedule.run_pending()
    time.sleep(1)


# In[ ]:


stalks = {}

fno_list = ['L&TFH', 'M&M','SBICARD']

# optionPremium(symbol,spot_entry,SL_points,position)


# In[25]:


data = getStockData("HDFCLIFE.NS","1d", '5m')
refactorData(data)
data


# In[ ]:




