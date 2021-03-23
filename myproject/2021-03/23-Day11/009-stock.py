import matplotlib.pyplot as plt
import numpy as np
import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

dateList = []
openList = []
closeList = []
fiveDayAvgCloseList = []
closeOpenDiffList = []
volumeList = []
with open(path+'2330.TW.csv', 'r', encoding="utf-8") as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)

    maxOpenClose = 0
    maxOpen = 0
    oldOpen = 0
    maxClose = 0
    oldClose = 0
    maxVolume = 0
    oldVolume = 0
    for row in read:
        dateList.append(row[0])

        try:
            open1 = float(row[1])
            oldOpen = row[1]
        except:
            open1 = float(oldOpen)

        try:
            close = float(row[4])
            oldClose = row[4]
        except:
            close = float(oldClose)

        try:
            volume = int(row[6])
            oldVolume = row[6]
        except:
            volume = int(oldVolume)

        if open1 > maxOpen:
            maxOpen = open1
        if close > maxClose:
            maxClose = close
        if volume > maxVolume:
            maxVolume = volume
        openClose = open1-close
        if openClose > maxOpenClose:
            maxOpenClose = openClose

        openList.append(open1)
        closeList.append(close)
        volumeList.append(volume)
        closeOpenDiffList.append(openClose)

    fiveDaySum = 0
    for i in range(4):
        fiveDaySum += closeList[i]
        fiveDayAvg = fiveDaySum/(i+1)
        fiveDayAvgCloseList.append(fiveDayAvg)

    for i in range(4, len(closeList)):
        fiveDaySum = 0
        for j in range(5):
            fiveDaySum += closeList[i-j]
        fiveDayAvg = fiveDaySum/5
        fiveDayAvgCloseList.append(fiveDayAvg)

    plt.title('2330 close')
    plt.subplot(12, 1, (1, 6))
    plt.plot(dateList, fiveDayAvgCloseList, 'b-', label="五日均線")
    plt.plot(dateList, openList, 'g-', label="開盤價")
    plt.plot(dateList, closeList, 'r-', label="收盤價")
    plt.xticks(np.arange(0, len(dateList)+10, len(dateList)//4))
    plt.yticks(np.arange(0, maxClose+10, maxClose//14))
    plt.legend()

    plt.subplot(12, 1, (8, 9))
    plt.plot(dateList, volumeList, 'r-', label="成交量")
    plt.xticks(np.arange(0, len(dateList)+10, len(dateList)//4))
    plt.yticks(np.arange(0, maxVolume+10, maxVolume//4))
    plt.legend()

    plt.subplot(12, 1, (11, 12))
    plt.plot(dateList, closeOpenDiffList, 'k-', label="單日漲跌幅")
    plt.xticks(np.arange(0, len(dateList)+10, len(dateList)//4))
    plt.yticks(np.arange(0-maxOpenClose-5, maxOpenClose+5, maxOpenClose*2//4))
    plt.legend()

    plt.show()
