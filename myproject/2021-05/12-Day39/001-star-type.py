from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('Stars.csv')

df['Color_Code'] = df['Color'].astype("category").cat.codes
df['Spectral_Class_Code'] = df['Spectral_Class'].astype("category").cat.codes

print(df.head(20))
x = df[["Temperature", "L", "R", "A_M", "Spectral_Class_Code",
        "Spectral_Class_Code", "Spectral_Numer"]].to_numpy()
y = df["Type"].to_numpy()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

number_of_species=df['Type'].max()+1

print("實際答案:", y_test)
print("--------------------LinearRegression--------------------")
reg = linear_model.LinearRegression().fit(x_train, y_train)
y_test_predict = np.array([round(x) for x in reg.predict(x_test)])
print("預測答案:", y_test_predict)
print('準確率:', metrics.accuracy_score(y_test, y_test_predict))

print("--------------------KNN--------------------")
knn = KNeighborsClassifier().fit(x_train, y_train)
y_test_predict = knn.predict(x_test)
print("預測答案:", y_test_predict)
print('準確率:', metrics.accuracy_score(y_test, y_test_predict))

print("--------------------K-means--------------------")
kmeans = KMeans(n_clusters=number_of_species).fit(x_train)
y_test_predict = kmeans.predict(x_test)
print("預測答案:", y_test_predict)
print('準確率:', metrics.accuracy_score(y_test, y_test_predict))

print("--------------------DecisionTree--------------------")
decisionTree = tree.DecisionTreeClassifier().fit(x_train, y_train)
tree.export_graphviz(decisionTree, out_file='tree.dot')
y_test_predict = decisionTree.predict(x_test)
print("預測答案:", y_test_predict)
print('準確率:', metrics.accuracy_score(y_test, y_test_predict))

print("--------------------RandomForest--------------------")
random_forest = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=2
).fit(x_train, y_train)
y_test_predict = random_forest.predict(x_test)
print("預測答案:", y_test_predict)
print('準確率:', metrics.accuracy_score(y_test, y_test_predict))

print("--------------------NaiveBayes--------------------")
naive_bayes = GaussianNB().fit(x_train, y_train)
y_test_predict = naive_bayes.predict(x_test)
print("預測答案:", y_test_predict)
print('準確率:', metrics.accuracy_score(y_test, y_test_predict))

print("--------------------Seaborn--------------------")
df2 = df[["Temperature", "L", "R", "A_M", "Color_Code",
          "Spectral_Class_Code", "Spectral_Numer", "Type"]]
sns.pairplot(
    data=df2,
    hue='Type',
    diag_kws={"hue": None, "color": ".2"},
    palette=sns.color_palette("husl", number_of_species)
)
print("image")
plt.show()
