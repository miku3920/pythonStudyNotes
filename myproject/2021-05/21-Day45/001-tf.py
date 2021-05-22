import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense
from tensorflow.keras import models
from tensorflow.keras import utils
import numpy as np
import pandas as pd
import seaborn as sns


def CreateDatasets(high, iNum, iArraySize):
    x_train = np.random.random((iNum, iArraySize)) * float(high)
    y_train = ((x_train[:iNum, 0] + x_train[:iNum, 1]) / 2).astype(int)     # 取整數
    return x_train, y_train, utils.to_categorical(y_train, num_classes=(high))


category = 10
dim = 2
x_train, y_train, y_train2 = CreateDatasets(category, 1000, dim)  # 建立全部1000個二維的訓練特徵值X因，而訓練結果Y 有10種答案


# 建立模型
model = models.Sequential()
model.add(Dense(10, activation='relu', input_dim=dim))
model.add(Dense(10, activation='relu'))
model.add(Dense(category, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train2, epochs=2000, batch_size=10)

# 測試
x_test, y_test, y_test2 = CreateDatasets(category, 10, dim)
score = model.evaluate(x_test, y_test2)
print("score:", score)

predict = model.predict(x_test)
print("Ans:", np.argmax(predict[0]), np.argmax(predict[1]), np.argmax(predict[2]), np.argmax(predict[3]))

predict2 = np.argmax(model.predict(x_test), axis=-1)
print("predict_classes:", predict2)
print("y_test", y_test[:])


print(x_train.shape)
print(y_train.shape)

df = pd.DataFrame({
    'x_0': x_train[:, 0],
    'x_1': x_train[:, 1],
    'y': y_train
})
sns.pairplot(data=df, kind='scatter', hue='y')
plt.show()
