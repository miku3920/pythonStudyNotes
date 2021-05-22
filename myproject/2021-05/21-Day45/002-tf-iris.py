import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras import models
from tensorflow.keras import utils
import numpy as np
import pandas as pd
import seaborn as sns

iris = datasets.load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

category = len(np.unique(y_train))
dim = x_train.shape[1]

# one-hot encoding
y_train2 = utils.to_categorical(y_train, num_classes=(category))
y_test2 = utils.to_categorical(y_test, num_classes=(category))

# 建立模型
model = models.Sequential()
model.add(Dense(10, input_shape=(dim,), activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(category))

model.compile(
    optimizer='adam',
    loss='hinge',
    metrics=['accuracy']
)
model.fit(x_train, y_train2, epochs=200, batch_size=5)

# 測試
score = model.evaluate(x_test, y_test2)
print("score:", score)

predict = model.predict(x_test)
print("Ans:", np.argmax(predict[0]), np.argmax(predict[1]), np.argmax(predict[2]), np.argmax(predict[3]))

predict2 = np.argmax(model.predict(x_test), axis=-1)
print("predict_classes:", predict2)
print("y_test", y_test[:])

print(x_train.shape)
print(np.unique(y_train))

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
sns.pairplot(data=df, kind='scatter', hue='species')
plt.show()
