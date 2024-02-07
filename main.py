import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta

#Preparing data from yahoo
today = date.today()    
end_date= today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=730)).strftime("%Y-%m-%d")


#get data from yahoo
data= yf.download("BTC-USD", start=start_date, end=end_date,progress=False)
print(data)
