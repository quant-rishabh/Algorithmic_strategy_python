#!/usr/bin/env python
# coding: utf-8

# In[70]:


#uptrend stocks
def breakout():
    for stalk in fno_list:
        if stalk not in visited.keys():
            data = getStockData(stalk)
            if data is not None:

                sh=data.index[data['swing_high'] == True].tolist()
                sd=data.index[data['swing_low'] == True].tolist()
                


                #remove very recent fake pivot .. that is second index
                
                #before trading hours comment below line
                
                
                if 70 in sh:
                    sh.remove(70)
                if 70 in sd:
                    sd.remove(70)

                
                if(len(sh)>2 ):
        
                    if((data['High'][sh[0]] <= data['High'][sh[1]]) or (data['High'][sh[0]] <= data['High'][sh[2]]) ):
                        
                        min_data = getStockData(stalk,5)
                        if min_data is not None : 
                            if(min_data['Close'][71] > data['High'][sh[0]]):

                                optionPremium(stalk,min_data['Close'][71],"long")

                                visited[stalk] = True
                if(len(sd)>2 ):
                    if((data['Low'][sd[0]] >= data['Low'][sd[1]]) or (data['Low'][sd[0]] >= data['Low'][sd[2]])):
                        min_data = getStockData(stalk,5)
                        if min_data is not None : 
                            if(min_data['Close'][71] < data['Low'][sd[0]]):
                                optionPremium(stalk,min_data['Close'][71],"short")
                                visited[stalk] = True
    print(visited.keys())


# In[14]:


#stalk to search before morning hours
def breakout():
    for stalk in fno_list:
        if stalk not in visited.keys():
            data = getStockData(stalk)
            if data is not None:

                sh=data.index[data['swing_high'] == True].tolist()
                sd=data.index[data['swing_low'] == True].tolist()
                


                #remove very recent fake pivot .. that is second index
                
                #before trading hours comment below line
                
                
                if 70 in sh:
                    sh.remove(70)
                if 70 in sd:
                    sd.remove(70)

                valid_range = 0.1
    
                if(len(sh)>2 ):
        
                    if((data['High'][sh[0]] <= data['High'][sh[1]]) or (data['High'][sh[0]] <= data['High'][sh[2]]) ):
                        
                        min_data = getStockData(stalk,15)
                        pivot = data['High'][sh[0]] + data['High'][sh[0]] *valid_range
                        if min_data is not None : 
                            if((min_data['swing_high'][70] <= pivot) and (min_data['swing_high'][70] >data['High'][sh[0]] ) ):
                                print(stalk,"up")
                                optionPremium(stalk,min_data['Close'][71],"long")

                                visited[stalk] = True
                if(len(sd)>2 ):
                    if((data['Low'][sd[0]] >= data['Low'][sd[1]]) or (data['Low'][sd[0]] >= data['Low'][sd[2]])):
                        min_data = getStockData(stalk,15)
                        pivot = data['Low'][sd[0]] - data['Low'][sd[0]] *valid_range
                        if min_data is not None : 
                            if((min_data['swing_low'][70] >= pivot) and (min_data['swing_low'][70] < data['Low'][sd[0]])):
                                optionPremium(stalk,min_data['Close'][71],"short")
                                visited[stalk] = True
                                print(stalk,"down")
    print(visited.keys())


# In[32]:


#uptrend stocks
def breakout():
    for stalk in fno_list:
        if stalk not in visited.keys():
            data = getStockData(stalk)
            if data is not None:

                sh=data.index[data['swing_high'] == True].tolist()
                sd=data.index[data['swing_low'] == True].tolist()
                


                #remove very recent fake pivot .. that is second index
                
                #before trading hours comment below line
                
                
                if 70 in sh:
                    sh.remove(70)
                if 70 in sd:
                    sd.remove(70)

                valid_range = 0.01
                
                if(len(sh)>3 ):
                    
                    if(((data['High'][sh[1]] <= data['High'][sh[2]]) or (data['High'][sh[1]] <= data['High'][sh[3]])) and (data['High'][sh[0]] > data['High'][sh[1]] )):
                        
                        min_data = getStockData(stalk,5)
                        pivot = data['High'][sh[0]] - data['High'][sh[0]] *valid_range
                        if min_data is not None : 
                            if(min_data['Close'][71] > pivot):
                                print(stalk,"Up ", pivot)
                                optionPremium(stalk,min_data['Close'][71],"long")

                                visited[stalk] = True
                if(len(sd)>3 ):
                    if(((data['Low'][sd[1]] >= data['Low'][sd[2]]) or (data['Low'][sd[1]] >= data['Low'][sd[3]])) and (data['Low'][sd[0]] < data['Low'][sd[1]])):
                        
                        min_data = getStockData(stalk,5)
                        pivot = data['Low'][sd[0]] + data['Low'][sd[0]] *valid_range
                        
                        
                        if min_data is not None : 
                           
                            if(min_data['Close'][71] < pivot):
                                print(stalk,"down ", pivot)
                                optionPremium(stalk,min_data['Close'][71],"short")
                                visited[stalk] = True
    print(visited.keys())


# In[1]:


import talib as ta
import yfinance as yf
import pandas as pd
import numpy as np
import time

import requests
import schedule
import datetime
import time


# In[2]:


fno_list = [ 'ADANIENT', 'RAIN', 'HINDCOPPER', 'NATIONALUM', 'ABCAPITAL', 'BHEL', 'DELTACORP', 'JINDALSTEL', 'HAL', 'FEDERALBNK', 'VEDL', 'HINDALCO', 'PNB', 'AMBUJACEM', 'INDIACEM', 'IBULHSGFIN', 'RBLBANK', 'BANKBARODA', 'L&TFH', 'NMDC', 'SRF', 'CANBK', 'GNFC', 'CHAMBLFERT', 'AUBANK', 'SAIL', 'DEEPAKNTR', 'ABB', 'PFC', 'UPL', 'MANAPPURAM', 'JKCEMENT', 'BEL', 'ABFRL', 'SBIN', 'CUMMINSIND', 'RAMCOCEM', 'INDUSINDBK', 'AXISBANK', 'TECHM', 'PERSISTENT', 'TCS', 'SUNTV', 'IDEA', 'CUB', 'CROMPTON', 'LICHSGFIN', 'INDIAMART', 'HCLTECH', 'HONAUT', 'ACC', 'DALBHARAT', 'MCX', 'IDFC', 'TATACHEM', 'LTTS', 'AARTIIND', 'METROPOLIS', 'UBL', 'MOTHERSON', 'BANDHANBNK', 'COROMANDEL', 'IEX', 'SHRIRAMFIN', 'INTELLECT', 'NAVINFLUOR', 'ZEEL', 'ONGC', 'CONCOR', 'TATASTEEL', 'INDHOTEL', 'JSWSTEEL', 'GUJGASLTD', 'GODREJPROP', 'EXIDEIND', 'COALINDIA', 'HAVELLS', 'BALKRISIND', 'MPHASIS', 'ADANIPORTS', 'BOSCHLTD', 'MARUTI', 'M&MFIN', 'ZYDUSLIFE', 'GRANULES', 'BALRAMCHIN', 'PIIND', 'IOC', 'CHOLAFIN', 'TATAMOTORS', 'ATUL', 'BAJAJ-AUTO', 'GMRINFRA', 'ABBOTINDIA', 'WIPRO', 'TRENT', 'DIXON', 'EICHERMOT', 'DLF', 'PVR', 'GRASIM', 'BHARTIARTL', 'MGL', 'IDFCFIRSTB', 'ASTRAL', 'RELIANCE', 'KOTAKBANK', 'TATAPOWER', 'PEL', 'BHARATFORG', 'VOLTAS', 'MRF', 'TORNTPHARM', 'BAJAJFINSV', 'MARICO', 'BSOFT', 'DRREDDY', 'NAUKRI', 'NTPC', 'DIVISLAB', 'BAJFINANCE', 'COLPAL', 'HEROMOTOCO', 'FSL', 'SYNGENE', 'INFY', 'GAIL', 'POLYCAB', 'RECLTD', 'OBEROIRLTY', 'APOLLOTYRE', 'SIEMENS', 'ASIANPAINT', 'SHREECEM', 'TORNTPOWER', 'NESTLEIND', 'ITC', 'JUBLFOOD', 'LUPIN', 'LT', 'TITAN', 'MCDOWELL-N', 'M&M', 'HDFC', 'LTIM', 'MFSL', 'SUNPHARMA', 'AUROPHARMA', 'IRCTC', 'BERGEPAINT', 'CANFINHOME', 'WHIRLPOOL', 'PAGEIND', 'HDFCLIFE', 'TATACONSUM', 'SBICARD', 'ICICIBANK', 'HINDUNILVR', 'ULTRACEMCO', 'TATACOMM', 'ESCORTS', 'BATAINDIA', 'SBILIFE', 'APOLLOHOSP', 'HDFCAMC', 'PIDILITIND', 'LAURUSLABS', 'IGL', 'HINDPETRO', 'HDFCBANK', 'INDUSTOWER', 'ICICIGI', 'GLENMARK', 'IPCALAB', 'OFSS', 'BPCL', 'BIOCON', 'ICICIPRULI', 'PETRONET', 'CIPLA', 'DABUR', 'INDIGO', 'ASHOKLEY', 'LALPATHLAB', 'MUTHOOTFIN', 'GODREJCP', 'POWERGRID', 'ALKEM', 'BRITANNIA', 'TVSMOTOR']


def getStockData(symbol, inter = '60'):
    response = requests.get(f"https://intradayscreener.com/api/CandlestickAnalysis/chartData/{symbol}/{inter}")
    time.sleep(0.2)
    if(response.ok):
        
        dta = response.json()['data']
        lst = []
       
        #x is volume
        #y is ohlc
        if dta is not None:
            for obj in dta:
                dt = datetime.datetime.fromtimestamp(obj['x']/1000.0)

                datetime_string=dt.strftime( "%d-%m-%Y %H:%M:%S" )
                obj['y'].append(datetime_string)
                lst.append(obj['y'])
            df = pd.DataFrame(lst, columns = ['Open', 'High', 'Low', 'Close','Time'])
            refactorData(df)
            return df
    return None



def refactorData(data):
#     data.drop(['Volume', 'Dividends','Stock Splits'], axis=1,inplace=True)
    data["atr"] = ta.ATR(data['High'], data['Low'], data['Close'],14)
    data['trailing_ATR'] = 0
    data['atr'] = data['atr'].fillna(0)
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

def optionPremium(symbol,spot_entry,position):
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
        print(symbol,spot_entry,position )
    if(position=="long"):
        Strike_price = strike_prices[call_ind]['strike_price']
        entry = strike_prices[call_ind]['calls_ltp']
        delta = strike_prices[call_ind]['call_delta']
        
        send_to_telegram(symbol + " " + str(Strike_price) + " CE \U0001F49A"  + '\n Spot Price : ' + str(spot_entry))
        return True
    
    Strike_price = strike_prices[put_ind]['strike_price']
    entry = strike_prices[put_ind]['puts_ltp']
    delta = strike_prices[put_ind]['put_delta']

    send_to_telegram(symbol + " " + str(Strike_price) + " PE \u2764\ufe0f"  + '\n Spot Price : ' + str(spot_entry))
    return True


# In[26]:


# get hourly data for 1st time and save in dictionary

map_Hour = {}

for stalk in fno_list:
    data = getStockData(stalk,"15")
    if data is not None and len(data)==73:
        ATRMultiplier = 1.5

        for i in range(14,len(data)):
            if((data.loc[i, "Close"] > data.loc[i-1, "trailing_ATR"]) and ((data.loc[i-1, "Close"]) > data.loc[i-1, "trailing_ATR"] ) ):
                data.loc[i, "trailing_ATR"] = max(data.loc[i-1, "trailing_ATR"], data.loc[i, "Close"] - data.loc[i,"atr"]*ATRMultiplier)

            elif ((data.loc[i, "Close"] < data.loc[i-1, "trailing_ATR"]) and ((data.loc[i-1, "Close"]) < data.loc[i-1, "trailing_ATR"] ) ):
                data.loc[i, "trailing_ATR"] = min(data.loc[i-1, "trailing_ATR"], data.loc[i, "Close"] + data.loc[i,"atr"]*ATRMultiplier)

            elif (data.loc[i, "Close"] >  data.loc[i-1, "trailing_ATR"]):
                data.loc[i, "trailing_ATR"] = data.loc[i, "Close"] - data.loc[i,"atr"]*ATRMultiplier

            else:
                data.loc[i, "trailing_ATR"] = data.loc[i, "Close"] + data.loc[i,"atr"]*ATRMultiplier
        
        map_Hour[stalk] = data.loc[72, "trailing_ATR"]


# In[27]:


map_Hour['TITAN']


# In[20]:


gap_percent = 0.5/100
stk_list = []
for stalk in fno_list:
    if stalk in map_Hour.keys():
        min_data = getStockData(stalk,15)
        if min_data is not None :
            val = map_Hour[stalk]
            upperBound = val + val*gap_percent
            lowerBound = val - val*gap_percent
            if((min_data['High'][72] <= upperBound) and (min_data['Close'][72] <= val) and (min_data['High'][72] >= lowerBound) ):
                stk_list.append(stalk)
#             elif((min_data['Close'][72] <= upperBound) and (min_data['Low'][72] >= lowerBound)  ):
#                 stk_list.append(stalk)
print(stk_list)            


# In[24]:


gap_percent = 0.5/100
stk_list = []
for stalk in fno_list:
    if stalk in map_Hour.keys():
        min_data = getStockData(stalk,5)
        if min_data is not None :
            val = map_Hour[stalk]
            upperBound = val + val*gap_percent
            lowerBound = val - val*gap_percent
            if((min_data['Low'][72] <= upperBound) and (min_data['Close'][72] >= val) and (min_data['High'][72] >= lowerBound) ):
                stk_list.append(stalk)
#             elif((min_data['Close'][72] <= upperBound) and (min_data['Low'][72] >= lowerBound)  ):
#                 stk_list.append(stalk)
print(stk_list) 


# In[15]:


map_Hour['NMDC']


# In[78]:


trailing_atr_lst = np.zeros(15, dtype = float)
ATRMultiplier = 1.5


data.loc[0, "fsf"] = 0 
for i in range(14,len(data)):
    if((data.loc[i, "Close"] > data.loc[i-1, "trailing_ATR"]) and ((data.loc[i-1, "Close"]) > data.loc[i-1, "trailing_ATR"] ) ):
        data.loc[i, "trailing_ATR"] = max(data.loc[i-1, "trailing_ATR"], data.loc[i, "Close"] - data.loc[i,"atr"]*ATRMultiplier)
        data.loc[i, "fsf"] = 1
    elif ((data.loc[i, "Close"] < data.loc[i-1, "trailing_ATR"]) and ((data.loc[i-1, "Close"]) < data.loc[i-1, "trailing_ATR"] ) ):
        data.loc[i, "trailing_ATR"] = min(data.loc[i-1, "trailing_ATR"], data.loc[i, "Close"] + data.loc[i,"atr"]*ATRMultiplier)
        data.loc[i, "fsf"] = 2 
    elif (data.loc[i, "Close"] >  data.loc[i-1, "trailing_ATR"]):
        data.loc[i, "trailing_ATR"] = data.loc[i, "Close"] - data.loc[i,"atr"]*ATRMultiplier
        data.loc[i, "fsf"] = 3 
    else:
        data.loc[i, "trailing_ATR"] = data.loc[i, "Close"] + data.loc[i,"atr"]*ATRMultiplier
        data.loc[i, "fsf"] = 4
data.loc[72, "trailing_ATR"]


# In[31]:


#trailing atr

ATRPeriod  =14
ATRMultiplier = 1.5


conditions = [
    ((data['Close'] >= data['trailing_ATR'].shift(-1) ) & (data['Close'].shift(-1)  >= data['trailing_ATR'].shift(-1)) & (data['trailing_ATR'].shift(-1)> data['Close'] - data['atr']*ATRMultiplier)) ,
    ((data['Close'] >= data['trailing_ATR'].shift(-1) ) & (data['Close'].shift(-1)  >= data['trailing_ATR'].shift(-1)) & (data['trailing_ATR'].shift(-1)< data['Close'] - data['atr']*ATRMultiplier) ),
    
    ((data['Close'] <= data['trailing_ATR'].shift(-1) )  & (data['Close'].shift(-1)  <= data['trailing_ATR'].shift(-1)) & (data['trailing_ATR'].shift(-1)< data['Close'] + data['atr']*ATRMultiplier)),
    ((data['Close'] <= data['trailing_ATR'].shift(-1) )  & (data['Close'].shift(-1)  <= data['trailing_ATR'].shift(-1)) & (data['trailing_ATR'].shift(-1)> data['Close'] + data['atr']*ATRMultiplier)),
    
    (data['Close'] > data['trailing_ATR'].shift(-1) ),
    (data['Close'] < data['trailing_ATR'].shift(-1) ),
    
    
]
values =[
    data['trailing_ATR'].shift(-1),
    data['Close'] - data['atr']*ATRMultiplier,  
    
    data['trailing_ATR'].shift(-1), 
    data['Close'] + data['atr']*ATRMultiplier,
    
    data['Close'] - data['atr']*ATRMultiplier,
    data['Close'] + data['atr']*ATRMultiplier
]

values2 =[
    1,
    2, 
    3, 
    4,
    5,
    6
]


data['trailing_ATR'] = np.select(conditions,values)
data["shift_atr"] = data['trailing_ATR'].shift(-1)
data['cond'] = np.select(conditions,values2, 1000)
data.tail(30)




# In[17]:


data = getStockData("RELIANCE","60")

data


# In[ ]:


#stalks near atr
def breakout():
    for stalk in fno_list:
        if stalk not in visited.keys():
            data = getStockData(stalk)
            if data is not None:
                min_data = getStockData(stalk,5)
                        if min_data is not None :
               
    print(visited.keys())


# In[68]:


#uptrend stocks
def breakout():
    for stalk in fno_list:
        if stalk not in visited.keys():
            data = getStockData(stalk)
            if data is not None:

                sh=data.index[data['swing_high'] == True].tolist()
                sd=data.index[data['swing_low'] == True].tolist()
                


                #remove very recent fake pivot .. that is second index
                
                #before trading hours comment below line
                
                
                if 70 in sh:
                    sh.remove(70)
                if 70 in sd:
                    sd.remove(70)



# breakout UP SIDE
                
                if(len(sh)>3 ):
                    
                        if(((data['High'][sh[1]] <= data['High'][sh[2]]) or (data['High'][sh[1]] <= data['High'][sh[3]])) and (data['High'][sh[0]] > data['High'][sh[1]] )):
                        
                            
                                    print(stalk,"Up " )
                                    optionPremium(stalk,data['Close'][72],"long")

                                    visited[stalk] = True
# breakout DOWN SIDE                                
                if(len(sd)>3 ):
                   
                        if(((data['Low'][sd[1]] >= data['Low'][sd[2]]) or (data['Low'][sd[1]] >= data['Low'][sd[3]])) and (data['Low'][sd[0]] < data['Low'][sd[1]])):
                        
                        
                            print(stalk,"down ")
                            optionPremium(stalk,data['Close'][72],"short")
                            visited[stalk] = True
    print(visited.keys())


# In[71]:


visited = {}
breakout()


# In[59]:


fno_list = ["IBULHSGFIN"]
visited = {}
breakout()


# In[9]:


import time
import requests
import schedule

visited = {}

def mainJob():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("starting at ", current_time)
    breakout()

#starting timing    
schedule.every(5).minutes.do(mainJob).until("15:30:15")

while(True):
    schedule.run_pending()
    time.sleep(1)


# In[49]:


print(near_breakdown)


# In[56]:


data = getStockData("IBULHSGFIN","60")
data[data["swing_high"]==True]


# In[101]:


sh=data.index[data['swing_high'] == True].tolist()

if((data['High'][sh[0]] <= data['High'][sh[1]]) and (data['High'][sh[0]] <= data['High'][sh[2]]) and (data['Close'][72] > data['High'][sh[0]])):
    print(stalk, " up")
    near_breakout.append(stalk)
data['Close'][72]


# In[ ]:






