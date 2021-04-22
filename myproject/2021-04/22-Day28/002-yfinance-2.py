import pandas as pd
df = pd.read_excel('AAPL.xlsx', 'AAPL')
print(df.head())
print(type(df))

print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
