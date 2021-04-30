from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

x = np.array([
    # 柳丁
    # 寬, 高
    [9.0, 9.0],
    [9.2, 9.2],
    [9.6, 9.2],
    [9.2, 9.2],
    [6.7, 7.1],
    [7.0, 7.4],
    [7.6, 7.5],
    # 檸檬
    [7.2, 10.3],
    [7.3, 10.5],
    [7.2, 9.2],
    [7.3, 10.2],
    [7.2, 9.7],
    [7.3, 10.1],
    [7.3, 10.1]
])
y = np.array([
    0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1
])


neigh = KNeighborsClassifier(n_neighbors=5)

neigh.fit(x, y)
print("預測答案＝", neigh.predict([[7, 9]]))
print("預測樣本距離＝", neigh.predict_proba([[7, 9]]))


plt.plot(x[:7, :1], x[:7, -1:], 'yx')
plt.plot(x[7:, :1], x[7:, -1:], 'g.')
plt.plot([7], [9], 'r^')
circle1 = plt.Circle((7, 9), 1.2, color='#aaaaaa')  # 1.2直徑
plt.gcf().gca().add_artist(circle1)

plt.axis([6, 11, 6, 11])
plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange', 'Lemons'), loc='upper right')
plt.show()