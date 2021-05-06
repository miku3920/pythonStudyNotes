import matplotlib.pyplot as plt
import pandas as pd

df = onestock = pd.read_excel('2330.xlsx', '2330')

close = onestock['Close']

short_rolling_msft = close.rolling(window=5).mean()
long_rolling_msft = close.rolling(window=10).mean()

onestock['SMA5'] = short_rolling_msft
onestock['SMA10'] = long_rolling_msft

fig, ax = plt.subplots(figsize=(16, 9))

ax.plot(close.index, close, label='2330')
ax.plot(short_rolling_msft.index, short_rolling_msft, label='5 days rolling')
ax.plot(long_rolling_msft.index, long_rolling_msft, label='10 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()
plt.show()
