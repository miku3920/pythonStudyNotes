from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 1
print('----------------------第一題----------------------')
df = pd.read_csv('臺北市統一發票.csv', encoding='big5')
print('----- head -----')
print(df.head())
print('----- info -----')
print(df.info())
print('----- describe -----')
print(df.describe())

# 2
print('----------------------第二題----------------------')
df[df['全年銷售額[千元]'] == '-'] = 0
df[df['全年使用張數[張]'] == '-'] = 1

df['全年銷售額[千元]'] = df['全年銷售額[千元]'].astype('int64')
df['全年使用張數[張]'] = df['全年使用張數[張]'].astype('int64')

df['每一張平均銷售額'] = df['全年銷售額[千元]']/df['全年使用張數[張]']
df['每一家平均銷售額'] = df['全年銷售額[千元]']/df['年底使用家數[家]']
print(df)

# 3
print('----------------------第三題----------------------')
print(df[df['稅別'] == '一般稅額']['全年銷售額[千元]'])

# 4
print('----------------------第四題----------------------')
df2 = pd.DataFrame()
df2['全年銷售額[千元]'] = df[df['稅別'] == '一般稅額']['全年銷售額[千元]']
df2['年別'] = df[df['稅別'] == '一般稅額']['年別']
print('圖片')
df2.plot(x='年別', y='全年銷售額[千元]', grid=True, color='blue')
plt.show()

# 5
print('----------------------第五題----------------------')
sales_mean = df2['全年銷售額[千元]'].mean()
df2['label'] = 0
df2.loc[df2['全年銷售額[千元]'] > sales_mean, 'label'] = 1
# df2['label'] = df2['全年銷售額[千元]'] > sales_mean
print(df2)

# 6
print('----------------------第六題----------------------')
data = df2.to_numpy()
x = data[:, :1].astype(dtype='float')
y = data[:, 2].astype(dtype='float')
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

print("預測", knn.predict(x_test))
print("實際", y_test)
print('準確率: %.2f' % knn.score(x_test, y_test))

plt.plot(x, y, 'r.')
plt.show()
