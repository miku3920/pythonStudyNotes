import numpy as np
from sklearn.cluster import KMeans
from time import time
import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    [1, 1], [1.1, 0.9], [1.2, 1.2],
    [2, 2], [2.1, 1.9], [2.2, 2.1]
])
y = [
    1, 1, 1,
    0, 0, 0
]

kmeans = KMeans(n_clusters=2, random_state=0).fit(x)
print("集群中心的坐標:", kmeans.cluster_centers_)
print("預測:", kmeans.predict(x))
print("實際:", y)
print("預測[1, 1],[2.3,2.1]:", kmeans.predict([[1, 1], [2.3, 2.1]]))

plt.axis([0, 3, 0, 3])
plt.plot(x[:3, 0], x[:3, 1], 'yx')
plt.plot(x[3:, 0], x[3:, 1], 'g.')
plt.plot(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 'ro')
plt.xticks(())
plt.yticks(())
plt.show()
