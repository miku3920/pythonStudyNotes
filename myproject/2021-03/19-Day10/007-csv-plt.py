import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math
import csv

path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+'\\'

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv(path+'data.csv', header=None, encoding='utf-8').to_numpy()
data = np.transpose(data)
print(np.shape(data))

plt.ylabel('aaaaaaa')
for i in range(1, 7):
    rgb = (random.random(), random.random(), random.random())
    x = data[0:1, 2:][0]
    y = data[i:i+1, 2:][0]
    label = data[i:i+1, :1][0]
    plt.plot(x, y, c=rgb, label=label)

plt.xticks(np.arange(0, 746, 240))
plt.yticks(np.arange(0, 75, 5))

plt.legend()
plt.show()
