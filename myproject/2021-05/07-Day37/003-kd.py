import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from mpl_finance import candlestick_ohlc
from talib import abstract

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

df = df.rename(columns={
    "Date": "date",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Volume": "volume"
})

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ohlc = df.loc[:, ['date', 'open', 'high', 'low', 'close']]
ohlc['date'] = pd.to_datetime(ohlc['date'])
ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)
candlestick_ohlc(
    ax1, ohlc.values,
    width=0.6, colorup='green',
    colordown='red', alpha=0.8
)
ax1.set_title("K線圖")

df.set_index('date', inplace=True)
abstract.STOCH(df).plot(ax=ax2, figsize=(16, 8))
ax2.set_title("KD STOCH , KD值")

plt.show()
