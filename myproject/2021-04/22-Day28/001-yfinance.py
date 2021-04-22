from pandas import ExcelWriter
from pandas_datareader import data, wb
import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
# pip install yfinance
# pip install pandas_datareader

pd.core.common.is_list_like = pd.api.types.is_list_like

df = web.get_data_yahoo("AAPL", start="2018-01-01", end="2018-12-02")
print(df.head())
writer = pd.ExcelWriter('AAPL.xlsx')
df.to_excel(writer, 'AAPL')
writer.save()
