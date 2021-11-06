import pandas as pd
import numpy as np
import talib
#データは2021年11月3日まで記載してあります｡
def predict_window(window_size):
    df=pd.read_csv('GBP_USD.csv')
    df=df[['closing_price','open_price','high_price','low_price']]
    sma20=np.array(talib.SMA(df['closing_price'],timeperiod=20))
    sma50=np.array(talib.SMA(df['closing_price'],timeperiod=50))
    macd,macdsignal,macdhist=np.array(talib.MACD(df['closing_price'], fastperiod=12, slowperiod=26, signalperiod=9))
    rsi7=np.array(talib.RSI(df['closing_price'],timeperiod=7))
    rsi14=np.array(talib.RSI(df['closing_price'],timeperiod=14))
    closing_price=np.array(df['closing_price'])
    open_price=np.array(df['open_price'])
    low_price=np.array(df['low_price'])
    high_price=np.array(df['high_price'])

    t=[]
    len_data=len(df)
    recently=len_data-1
    window=len_data-window_size-1

    t.append(closing_price[window:recently])
    t.append(open_price[window:recently])
    t.append(low_price[window:recently])
    t.append(high_price[window:recently])
    t.append(sma20[window:recently])
    t.append(sma50[window:recently])
    t.append(macd[window:recently])
    t.append(rsi7[window:recently])
    t.append(rsi14[window:recently])

    price=closing_price[-1]
    return t,price
if __name__=='__main__':
    predict_window()