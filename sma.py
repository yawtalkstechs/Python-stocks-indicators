import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

'''
The Simple Moving Average (SMA) is calculated
by adding the price of an instrument over a number of time periods
and then dividing the sum by the number of time periods. The SMA
is basically the average price of the given time period, with equal
weighting given to the price of each period.

Simple Moving Average
SMA = ( Sum ( Price, n ) ) / n    

Where: n = Time Period

'''


start_date = '2010-01-01'
end_date = '2020-09-01'
symbol = 'MSFT'
source = 'yahoo'
stock_data = 'MSFT_data.pkl'

try:
	msft_data1 = pd.read_pickle(stock_data)
	print('Data found and successfully loaded')
except FileNotFoundError:
	print("Data Not Found, downloading data...")
	msft_data1 = data.DataReader(symbol, source, start_date, end_date)
	
msft_data = msft_data1.tail(620)
close = msft_data['Close']

time_period = 100
history = []
sma_values = []

for close_price in close:
	history.append(close_price)
	if len(history) > time_period:
		del (history[0])
		
	sma_values.append(np.mean(history))
	
msft_data = msft_data.assign(ClosePrice=pd.Series(close, index=msft_data.index))
msft_data = msft_data.assign(SMA100Days=pd.Series(sma_values, index=msft_data.index))

close_price = msft_data['ClosePrice']
sma = msft_data['SMA100Days']

fig = plt.figure()
ax1=fig.add_subplot(111, ylabel='Microsoft stock prices in $')
close_price.plot(ax=ax1, color='g', lw=2., legend=True)
sma.plot(ax=ax1, color='r', lw=2., legend=True)
plt.show()
