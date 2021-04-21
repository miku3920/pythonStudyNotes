import pandas as pd

df = pd.read_excel('ExpensesRecord.xls', 'sheet')
#df = pd.read_csv('ExpensesRecord.csv')
#df = pd.read_json('ExpensesRecord.json')
#df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df.head())

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet2')
writer.save()