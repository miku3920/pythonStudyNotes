from mpl_finance import candlestick_ohlc  # <----
import matplotlib.dates as mpl_dates
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

df = df.rename(columns={
    "Date": "date",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close"
})

ohlc = df.loc[:, ['date', 'open', 'high', 'low', 'close']]
ohlc['date'] = pd.to_datetime(ohlc['date'])
ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)

fig, ax = plt.subplots()
candlestick_ohlc(
    ax, ohlc.values,
    width=0.6, colorup='green',
    colordown='red', alpha=0.8
)
ax.set_xlabel('date')
ax.set_ylabel('close')
fig.suptitle('Daily Candlestick Chart of NIFTY50')

date_format = mpl_dates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()
fig.tight_layout()

plt.show()
