#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nsepy import get_history as gh
import datetime as dt
from matplotlib import pyplot as plt
from datetime import date
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import pandas as pd
from numpy import asarray
import numpy as np
import tensorflow as tf
tf.random.set_seed(
   0
)
from yahoo_fin import stock_info
np.random.seed(0)
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential, save_model
#from tensorflow.keras.callbacks import ModelCheckpoint
import math
import yfinance as yf
from pandas_datareader import data as pdr
from keras.models import load_model
from datetime import datetime, timedelta


# In[2]:


def pred(symbol):
    tf.random.set_seed(0)
    np.random.seed(0)
    start = dt.datetime(2016,1,1)
    today = date.today().strftime("%Y,%m,%d")
    year,mon,day=today.split(',')
    end = dt.datetime(int(year),int(mon),int(day))
   # end = dt.datetime(int(year),int(mon),int(day))- timedelta(days=2)
    print(end)
    stk_data =yf.download(tickers=symbol+'.NS',start=start,end=end, interval='1d')
    print(stk_data.tail())
   # stk_data = gh(symbol=symbol,start=start,end=end)
    #print(stk_data)
    Xt=np.array(stk_data['Open'])
    Yt=np.array(stk_data['Close'])
    X=[]
    for i in range(len(stk_data['Close'])):
        X.append(stk_data['Close'][i])
    for i in range(len(stk_data['Open'])):
        X.append(stk_data['Open'][i])

    
    xtrain, X_test, ytrain, y_test = train_test_split(Xt, Yt, random_state=0)
    xtraining_set_scaled = (np.array(xtrain).reshape(-1, 1))
    ytraining_set_scaled = (ytrain.reshape(-1, 1))
    X_train = []
    y_train = []
    X_train= np.array(xtraining_set_scaled)
    y_train=np.array(ytraining_set_scaled)

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    t=math.inf
    n_split=3

    for train_index,test_index in KFold(n_split,shuffle = False).split(X_train):
        xtrain,xtest=X_train[train_index],X_train[test_index]
        ytrain,ytest=y_train[train_index],y_train[test_index]
        sc = MinMaxScaler()
        sc.fit(xtrain.reshape(-1, 1))
       # sc.fit(ytrain.reshape(-1, 1))
        xtrain=sc.transform(np.array(xtrain).reshape(-1, 1))
        ytrain=sc.transform(np.array(ytrain).reshape(-1, 1))
        xtest=sc.transform(np.array(xtest).reshape(-1, 1))
        ytest=sc.transform(np.array(ytest).reshape(-1, 1))
        keras.backend.clear_session()
        regressor = Sequential()
        
        regressor.add(LSTM(units = 256, return_sequences = True, input_shape = (xtrain.shape[1], 1)))
        regressor.add(Dropout(0.25))
        regressor.add(LSTM(units = 256,  return_sequences = True))
        regressor.add(Dropout(0.25))
        regressor.add(LSTM(units = 256,  return_sequences = True))
        regressor.add(Dropout(0.25))

        regressor.add(LSTM(units = 256))
        regressor.add(Dropout(0.25))
    
        regressor.add(Dense(units = 512))
        regressor.add(Dense(units = 128))
        regressor.add(Dense(units = 8))
        regressor.add(Dense(units = 1))

        regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

        regressor.fit(xtrain, ytrain, epochs = 25, batch_size = 32,verbose=0)
    
        scores=regressor.evaluate(xtest,ytest)
        if scores<t:
            t=scores
            filepath = symbol+"scaleopen"
            save_model(regressor, filepath, save_format='h5')
    keras.backend.clear_session()
    regressor = load_model(symbol+"scaleopen")
    #year,mon,day=today.split(',')
    #today = date.today().strftime("%Y,%m,%d")
    #st = dt.datetime(int(year),int(mon),int(day))- timedelta(days=1)
    #end = dt.datetime(int(year),int(mon),int(day))
    #print("End",end)
    #yf.pdr_override()
    #totest=pdr.get_data_yahoo(symbol+".NS", start=st, end=end)
   # print(totest)
    #cl=totest['Open']
    #cl=[490.95,634.96,8465,479.54,608]
    sc = MinMaxScaler()
    sc.fit(np.array(X).reshape(-1, 1))
    data = yf.download(tickers=symbol+'.NS', period='1d', interval='15m')
    predicted_stock_price = regressor.predict(sc.transform(np.array(data['Open'][1]).reshape(-1, 1)))
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    print(data['Open'][1],symbol,"price is",predicted_stock_price,"for the date",end)
    


# In[3]:


#stocks=['ICICISENSX','SBIN','TATAELXSI','MARICO','WIPRO','ADANIPORTS','HDFCLIFE','ICICI','AXISBANK','LAURUSLABS',
 #      'IRCTC','IEX','SUNPHARMA','LXCHEM','ZENSARTECH','JSWENERGY','MFSL','HINDALCO','IDFC','TRIDENT','TATAPOWER',
  #     'HINDZINC','IRFC','CREDITACC','RAILTEL','SJS','NAM-INDIA']
stocks=['ICICISENSX','SBIN','TATAELXSI','MARICO','WIPRO']
for i in stocks:
    pred(i)


# In[4]:


stocks=['ADANIPORTS','HDFCLIFE','AXISBANK','LAURUSLABS']
for i in stocks:
    pred(i)
    


# In[5]:


stocks=['HINDZINC','IRFC','CREDITACC','RAILTEL','SJS','NAM-INDIA']
for i in stocks:
    pred(i)


# In[6]:


stocks=['IRCTC','IEX','SUNPHARMA','LXCHEM','ZENSARTECH','JSWENERGY']
for i in stocks:
    pred(i)


# In[7]:


stocks=['MFSL','HINDALCO','IDFC','TRIDENT','TATAPOWER','SBICARD']
for i in stocks:
    pred(i)


# In[8]:


stocks=['HCLTECH','INDUSINDBK','TATASTEEL','CIPLA','ESCORTS','JKCEMENT','KOTAKBANK']
for i in stocks:
    pred(i)


# In[2]:


def notrain(symbol):
    keras.backend.clear_session()
    tf.random.set_seed(0)
    np.random.seed(0)
    regressor = load_model(symbol+"scaleopen")
    start = dt.datetime(2016,1,1)
    today = date.today().strftime("%Y,%m,%d")
    year,mon,day=today.split(',')

    end = dt.datetime(int(year),int(mon),int(day))
    #print(end)
    #stk_data = gh(symbol=symbol,start=start,end=end)
    stk_data = yf.download(tickers=symbol+'.NS', period='6y', interval='1d')

    sc = MinMaxScaler()
    Xt=np.array(stk_data['Open'])
    Yt=np.array(stk_data['Close'])
    X=[]
    for i in range(len(stk_data['Close'])):
        X.append(stk_data['Close'][i])
    for i in range(len(stk_data['Open'])):
        X.append(stk_data['Open'][i])

    sc.fit(np.array(X).reshape(-1, 1))
    
    
    today = date.today().strftime("%Y,%m,%d")
    year,mon,day=today.split(',')
    st = dt.datetime(int(year),int(mon),int(day))- timedelta(days=2)
    end = dt.datetime(int(year),int(mon),int(day))
    #stk_data2 = gh(symbol=symbol,start=st,end=end)
    stk_data2 = yf.download(tickers=symbol+'.NS', period='3d', interval='1d')

    X_train=[]
    y_train=[]
    X_train=np.array(stk_data2['Open'])
    y_train=np.array(stk_data2['Close'])
    #print(X_train,y_train)
    xtraining_set_scaled = sc.transform(np.array(X_train).reshape(-1, 1))
    ytraining_set_scaled = sc.transform(y_train.reshape(-1, 1))
    X_train= np.array(xtraining_set_scaled)
    y_train=np.array(ytraining_set_scaled)
    #print(X_train,y_train)

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    #print(st,stk_data2)
   # regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

    #regressor.fit(X_train, y_train, epochs = 25, batch_size = 32,verbose=0)
    filepath = symbol+"2"
    #save_model(regressor, filepath, save_format='h5')
    #regressor = load_model(symbol+"2")

    ##totest=pdr.get_data_yahoo(symbol+".NS", start=st, end=end)
    #cl=totest['Open']
    #cl=[490.95,634.96,8465,479.54,608]
    data = yf.download(tickers=symbol+'.NS', period='1d', interval='15m')
    #print(data)
    #print("test data",sc.transform(np.array(data['Open'][0]).reshape(-1, 1)))

    predicted_stock_price = regressor.predict(sc.transform(np.array(data['Open'][1]).reshape(-1, 1)))
    #print(predicted_stock_price)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    print(data['Open'][1],symbol,"price is",predicted_stock_price,"for the date",end)


# In[3]:



stocks=['ICICISENSX','SBIN','TATAELXSI','MARICO','WIPRO','ADANIPORTS','HDFCLIFE','AXISBANK','LAURUSLABS',
       'IRCTC','SUNPHARMA','ZENSARTECH','MFSL','HINDALCO','IDFC','TATAPOWER',
       'HINDZINC','IRFC','CREDITACC','RAILTEL','SJS','NAM-INDIA','HCLTECH','INDUSINDBK','TATASTEEL','JKCEMENT','KOTAKBANK'
        ,'SBICARD','ESCORTS','LXCHEM','CIPLA']
#stocks=['ICICISENSX','SBIN','TATAELXSI','MARICO','WIPRO']
for i in stocks:
    notrain(i)


# In[ ]:


''' today = date.today().strftime("%Y,%m,%d")
 year,mon,day=today.split(',')
 
 st = dt.datetime(int(year),int(mon),int(day)-3)
 end = dt.datetime(int(year),int(mon),int(day)+1)
 #print("End",end)
 yf.pdr_override()
 totest=pdr.get_data_yahoo("ICICISENSX"+".NS", start=st, end=end)
 print(totest)
 '''


# In[ ]:


start = dt.datetime(2016,1,1)
today = date.today().strftime("%Y,%m,%d")
year,mon,day=today.split(',')

end = dt.datetime(int(year),int(mon),int(day))
stk_data = gh(symbol='ADANIPORTS',start=start,end=end)
    
sc = MinMaxScaler()
Xt=np.array(stk_data['Open'])
Yt=np.array(stk_data['Close'])
X=[]
for i in range(len(stk_data['Close'])):
    X.append(stk_data['Close'][i])
for i in range(len(stk_data['Open'])):
    X.append(stk_data['Open'][i])

sc.fit(np.array(X).reshape(-1, 1))
data = yf.download(tickers='ADANIPORTS.NS', period='2d', interval='1ds')
print(data)
print(data['Open'][0])
print(stock_info.get_live_price("ADANIPORTS.NS"))
regressor = load_model('ADANIPORTS')
predicted_stock_price = regressor.predict(sc.transform(np.array(783).reshape(-1, 1)))
predicted_stock_price = sc.inverse_transform(predicted_stock_price)


# In[ ]:


'''today = date.today().strftime("%Y,%m,%d")

year,mon,day=today.split(',')
st = dt.datetime(int(year),int(mon),int(day)-3)
end = dt.datetime(int(year),int(mon),int(day)+1)
totest=pdr.get_data_yahoo("ICICISENSX"+".NS", start=st, end=end)
print(totest)
cl=totest['Open']
'''


# In[ ]:


start = dt.datetime(2016,1,1)
today = date.today().strftime("%Y,%m,%d")
year,mon,day=today.split(',')

end = dt.datetime(int(year),int(mon),int(day))
data = yf.download(tickers='ADANIPORTS.NS', start=start,end=end, interval='90m')
print(data)


# In[ ]:


start = dt.datetime(2016,1,1)
today = date.today().strftime("%Y,%m,%d")
year,mon,day=today.split(',')
end = dt.datetime(int(year),int(mon),int(day))
data = yf.download(tickers='ICICISENSX'+'.NS',start=start,end=end, interval='1d')
print(data.tail())


# In[ ]:


print(stock_info.get_live_price("ADANIPORTS.NS"))


# In[ ]:


start = dt.datetime(2016,1,1)
today = date.today().strftime("%Y,%m,%d")
year,mon,day=today.split(',')
end = dt.datetime(int(year),int(mon),int(day))
   # end = dt.datetime(int(year),int(mon),int(day))- timedelta(days=2)
print(end)
stk_data =yf.download(tickers=+'.NS',start=start,end=end, interval='1d')
print(stk_data)


# In[ ]:




