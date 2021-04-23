import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())


# 3 filter'

print("--------------------")
print(df[df['Date'] == '2018-01-05'])
print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10')])
print(df[df['Open'] > 194.2])
print(df[['Date', 'Open']][:5])
print(df.sort_values(by=['Volume'])[:5])
print(df.sort_values(by=['Volume'], ascending=False)[:5])
print(df['Open'][:30].rolling(7).mean())


# 4 Calculation
print("--------------------")
df['diff'] = df['Close']-df['Open']
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
print(df.head())
print("April Volume sum=%.2f" % df[df['month'] == 4][['Volume']].sum())
print("April Open mean=%.2d" % df[df['month'] == 4][['Open']].mean())


#  5 matplotlib
df.plot(x='Date', y='Open', grid=True, color='blue')
plt.show()


df.plot(y='diff', grid=True, color='red', kind='hist')
plt.show()


fig, ax = plt.subplots()
# print(df.groupby('month')[0])   #  [1,2,3,4,5,6,7,8,9,10,11,12]


for name, group in df.groupby('month'):
    group.plot(x='day', y='Open', ax=ax, label=name)
plt.show()

fileds = ['Open', 'Close', 'High']
fig, ax = plt.subplots()
for name in fileds:
    df.plot(x='Date', y=name, ax=ax, label=name)
plt.show()

dfMonths = df.loc[df['month'].isin([1, 2, 3, 4, 5, 6, 7])]
print(dfMonths)
dfMonthsPivot = dfMonths.pivot_table(
    values='High', columns='month', index='day')
dfMonthsPivot.plot(kind='box', title='Months High')
plt.show()
