import matplotlib.pyplot as plt
import numpy as np
import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

with open(path+'2330.TW.csv', 'r', encoding="utf-8") as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)
    read = list(read)

    dateList = []
    openList = []
    closeList = []
    fiveDayAvgCloseList = []
    closeOpenDiffList = []
    volumeList = []

    maxOpenClose = 0
    maxOpen = 0
    oldOpen = 0
    maxClose = 0
    oldClose = 0
    maxVolume = 0
    oldVolume = 0
    fiveDaySum = 0
    for i in range(len(list(read))):
        dateList.append(read[i][0])

        try:
            open1 = float(read[i][1])
            oldOpen = read[i][1]
        except:
            open1 = float(oldOpen)

        try:
            close = float(read[i][4])
            oldClose = read[i][4]
        except:
            close = float(oldClose)

        try:
            volume = int(read[i][6])
            oldVolume = read[i][6]
        except:
            volume = int(oldVolume)

        if open1 > maxOpen:
            maxOpen = open1
        if close > maxClose:
            maxClose = close
        if volume > maxVolume:
            maxVolume = volume
        openClose = close-open1
        if openClose > maxOpenClose:
            maxOpenClose = openClose

        openList.append(open1)
        closeList.append(close)
        volumeList.append(volume)
        closeOpenDiffList.append(openClose)

        fiveDaySum += closeList[i]
        if i < 5:
            fiveDayAvg = fiveDaySum/(i+1)
        else:  # i >= 5
            fiveDaySum -= closeList[i-5]
            fiveDayAvg = fiveDaySum/5
        fiveDayAvgCloseList.append(fiveDayAvg)

    plt.subplot(12, 1, (1, 6))
    plt.plot(dateList, fiveDayAvgCloseList, 'b-', label="五日均線")
    plt.plot(dateList, openList, 'g-', label="開盤價")
    plt.plot(dateList, closeList, 'r-', label="收盤價")
    plt.xticks(np.arange(0, len(dateList)*1.1, len(dateList)//4))
    plt.yticks(np.arange(0, maxClose*1.1, maxClose//14))
    plt.title('2330')
    plt.legend()

    plt.subplot(12, 1, (8, 9))
    plt.plot(dateList, volumeList, 'r-', label="成交量")
    plt.xticks(np.arange(0, len(dateList)*1.1, len(dateList)//4))
    plt.yticks(np.arange(0, maxVolume*1.4, maxVolume//3))
    plt.legend()

    plt.subplot(12, 1, (11, 12))
    plt.plot(dateList, closeOpenDiffList, 'k-', label="收盤減開盤")
    plt.xticks(np.arange(0, len(dateList)*1.1, len(dateList)//4))
    plt.yticks(np.arange(0-maxOpenClose*1.5, maxOpenClose*2, maxOpenClose))
    plt.legend()

    plt.show()
