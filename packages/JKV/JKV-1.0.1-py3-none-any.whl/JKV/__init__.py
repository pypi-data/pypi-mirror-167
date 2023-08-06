#!/usr/bin/env python
# coding: utf-8

__version__ = "1.0.1"


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




def pred(symbol):
    tf.random.set_seed(0)
    np.random.seed(0)
    start = dt.datetime(2016,1,1)
    today = date.today().strftime("%Y,%m,%d")
    year,mon,day=today.split(',')
    end = dt.datetime(int(year),int(mon),int(day))

    stk_data =yf.download(tickers=symbol+'.NS',start=start,end=end, interval='1d')
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
    regressor = Sequential()

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

    sc = MinMaxScaler()
    sc.fit(np.array(X).reshape(-1, 1))
    data = yf.download(tickers=symbol+'.NS', period='1d', interval='15m')
    predicted_stock_price = regressor.predict(sc.transform(np.array(data['Open'][1]).reshape(-1, 1)))
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    print(data['Open'][1],symbol,"price is",predicted_stock_price,"for the date",end)
    


