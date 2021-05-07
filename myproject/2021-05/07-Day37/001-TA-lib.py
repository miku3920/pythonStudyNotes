from talib import abstract
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

df = df.rename(columns={"Close": "close", "Date": "date"})
df.set_index('date', inplace=True)
df['close'].plot(figsize=(16, 8), label='close')

abstract.SMA(df, 5).plot(figsize=(16, 8), label='SMA5')
abstract.SMA(df, 20).plot(figsize=(16, 8), label='SMA20')
abstract.SMA(df, 60).plot(figsize=(16, 8), label='SMA60')
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.title('AAPL Close')
plt.show()
