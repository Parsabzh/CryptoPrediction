import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go

#Preparing data from yahoo
today = date.today()    
end_date= today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=730)).strftime("%Y-%m-%d")


#get data from yahoo
data= yf.download("BTC-USD", start=start_date, end=end_date,progress=False)
data["Date"]= data.index
data=data[["Date","Open","High","Low","Close","Adj Close","Volume"]]
data.reset_index(drop=True,inplace=True)
print(data.head())

#plot the data
figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                       open=data["Open"],
                                       high=data["High"],
                                       low=data["Low"],
                                       close=data["Close"])])


figure.update_layout(title="BTC-USD",xaxis_rangeslider_visible=False)
figure.show()

#Correlation for "Close"
correlation= data.corr()
print(correlation["Close"].sort_values(ascending=False))