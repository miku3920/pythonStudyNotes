from os import path
from datetime import datetime
import requests
import csv


def getData(strDate='20140630', endDate='20210420', stockNo=''):
    dataPath = str(strDate)+'-'+str(endDate)+'-'+str(stockNo)+'.csv'

    if not path.exists(dataPath):
        csv1 = requests.get(
            'https://www.twse.com.tw/exchangeReport/TWTBAU2?response=csv&strDate='+strDate+'&endDate='+endDate+'&stockNo='+stockNo).text.replace("\r\n", "\n")
        with open(dataPath, 'w') as f:
            f.write(csv1)

    with open(dataPath, 'r') as f:
        return csv.reader(f, delimiter=',')
