from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

iris = datasets.load_iris()

iris_x_train, iris_x_test, iris_y_train, iris_y_test = train_test_split(
    iris.data, iris.target, test_size=0.2)


kmeans = KMeans(n_clusters=3)
kmeans_fit = kmeans.fit(iris_x_train)


print("實際", iris_y_test)
# print("預測",kmeans_fit.labels_)
iris_y_test[iris_y_test == 1] = 11
iris_y_test[iris_y_test == 0] = 1
iris_y_test[iris_y_test == 11] = 0
print("調整", iris_y_test)
print("預測", kmeans.predict(iris_x_test))

score = metrics.accuracy_score(iris_y_test, kmeans.predict(iris_x_test))
print('準確率:{0:f}'.format(score))
