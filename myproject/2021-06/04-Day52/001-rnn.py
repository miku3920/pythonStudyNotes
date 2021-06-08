# project 6
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

start = np.arange(0, 6, 1)
stop = np.arange(1434, 1440, 1)
ls = np.linspace(start, stop, 1435)
sin = np.sin(2 * np.pi * ls / 180) + np.random.normal(0, 1e-1, ls.shape)

x = sin[:720, :-1]
x = x.reshape(x.shape + (1,))
y = sin[:720, -1:]
x_test = sin[720:, :-1]
x_test = x_test.reshape(x_test.shape + (1,))
y_test = sin[720:, -1:]

print(x.shape)
print(y.shape)

# 建立模型
model = keras.Sequential()
model.add(keras.layers.SimpleRNN(5, 'relu', input_shape=(5, 1), return_sequences=True))
model.add(keras.layers.SimpleRNN(5, 'relu'))
model.add(keras.layers.Dense(5, 'relu'))
model.add(keras.layers.Dense(1))
print(model.summary())

model.compile(loss="mse", optimizer="adam")
model.fit(x, y, epochs=20)

model.evaluate(x, y)

predict = model.predict(np.concatenate((x, x_test)))
plt.plot(np.concatenate((y, y_test)), '.', color='black', markersize=3)
plt.plot(predict)
plt.show()
