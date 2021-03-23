import matplotlib.pyplot as plt
import numpy as np
import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

dateList = []
closeList = []
with open(path+'0050.TW.csv', 'r', encoding="utf-8") as fin:
    read = csv.reader(fin, delimiter=',')
    header = next(read)   # 讀擋頭
    print(header)
    old = 0
    maxClose = 0
    for row in read:
        dateList.append(row[0])
        try:
            x = float(row[4])
            if x > maxClose:
                maxClose = x
            closeList.append(x)
            old = row[4]
        except:
            closeList.append(float(old))

    plt.xticks(np.arange(0, len(dateList)+10, len(dateList)//5-10))
    plt.yticks(np.arange(0, maxClose+10, maxClose//8-10))

    plt.legend()
    plt.plot(dateList, closeList, 'r-')
    plt.title('0050 close')
    plt.show()


# 1. 印出所有資料
# 2. 最大 最小 平均

print("最大", max(closeList))
print("最小", min(closeList))
avg_value = 0 if len(closeList) == 0 else sum(closeList)/len(closeList)
print("平均", avg_value)


# 3. 畫出圖表
