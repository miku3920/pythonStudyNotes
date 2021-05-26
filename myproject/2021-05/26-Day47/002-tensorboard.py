import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from sklearn import datasets
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
from tensorflow.keras.callbacks import TensorBoard

# python -m tensorboard.main --logdir=logs/

iris = datasets.load_iris()

category = 3
dim = 4
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
y_train2 = tf.keras.utils.to_categorical(y_train, num_classes=(category))
y_test2 = tf.keras.utils.to_categorical(y_test, num_classes=(category))

print("x_train[:4]", x_train[:4])
print("y_train[:4]", y_train[:4])
print("y_train2[:4]", y_train2[:4])

# 建立模型
model = Sequential()
model.add(layers.Dense(10, activation='relu', input_dim=dim))
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(category, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

tensorboard = TensorBoard(log_dir="logs")
history = model.fit(
    x_train, y_train2,
    epochs=200, batch_size=10,
    callbacks=[tensorboard],
    verbose=1
)

# 測試
score = model.evaluate(x_test, y_test2)
print("score:", score)

predict = model.predict(x_test)
print("Ans:", np.argmax(predict[0]), np.argmax(predict[1]), np.argmax(predict[2]), np.argmax(predict[3]))

predict2 = np.argmax(model.predict(x_test), axis=-1)
print("predict_classes:", predict2)
print("y_test", y_test[:])
