from sklearn.decomposition import PCA, IncrementalPCA
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

x_test = np.array([[8, 8], [8.3, 8.3]])

x_pca = PCA().fit_transform(x)
x_i_pca = IncrementalPCA(n_components=2, batch_size=10).fit_transform(x)

plt.plot(x[:7, :1], x[:7, -1:], '.', color='#ff0000')
plt.plot(x[7:, :1], x[7:, -1:], '.', color='#00ff00')
plt.plot(x_pca[:7, :1], x_pca[:7, -1:], '.', color='#cc0000')
plt.plot(x_pca[7:, :1], x_pca[7:, -1:], '.', color='#00cc00')
plt.plot(x_i_pca[:7, :1], x_i_pca[:7, -1:], '.', color='#440000')
plt.plot(x_i_pca[7:, :1], x_i_pca[7:, -1:], '.', color='#004400')

plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange', 'Lemons'), loc='upper right')
plt.show()
