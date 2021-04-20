from os import path
from datetime import datetime
import requests
import csv

dataPath = str(datetime.now().strftime("%Y-%m-%d"))+'.csv'

if not path.exists(dataPath):
    csv1 = requests.get('https://www.twse.com.tw/exchangeReport/TWTBAU1?response=csv').text.replace("\r\n", "\n")
    with open(dataPath, 'w') as f:
        f.write(csv1)

with open(dataPath, 'r') as f:
    read = csv.reader(f, delimiter=',')
    header = next(read)
    print(header)
    header2 = next(read)
    print(header2)
    for row in read:
        print(row)
