import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from os import path
from tensorflow import keras
from keras import layers, optimizers, models
from keras.utils import np_utils
from keras.models import Sequential
import keras.backend as K
import numpy as np


if path.exists('x_train.npy'):
    x_train = np.load('x_train.npy')
    x_test = np.load('x_test.npy')
    y_train_onehot = np.load('y_train_onehot.npy')
    y_test_onehot = np.load('y_test_onehot.npy')

    randomize = np.arange(x_train.shape[0])
    np.random.shuffle(randomize)
    x_train = x_train[randomize]
    y_train_onehot = y_train_onehot[randomize]
else:
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()
    x_train = x_train / 255
    x_test = x_test / 255
    y_train_onehot = np_utils.to_categorical(y_train)
    y_test_onehot = np_utils.to_categorical(y_test)

    np.save('x_train', x_train)
    np.save('x_test', x_test)
    np.save('y_train_onehot', y_train_onehot)
    np.save('y_test_onehot', y_test_onehot)

print(x_train.shape)
print(y_train_onehot.shape)


def swish(x):
    return 1.67653251702 * x * K.sigmoid(x)


model_name = 'cifar.h5'
if path.exists(model_name):
    model = models.load_model(model_name)
else:
    model = Sequential()
    model.add(layers.Input(shape=(32, 32, 3)))
    for i in range(2):
        model.add(layers.Conv2D(2 ** (i + 5), (3, 3)))
        model.add(layers.Activation(swish))
        model.add(layers.Dropout(0.5))
        model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    for i in range(2):
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(2 ** (8 - i)))
        model.add(layers.Activation(swish))
    model.add(layers.Dense(y_train_onehot.shape[1]))
    model.add(layers.Activation('softmax'))

    model.compile(
        optimizer=optimizers.Adam(1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

callback = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    min_delta=0,
    patience=50,
    verbose=0,
    mode="min",
    baseline=None,
    restore_best_weights=True,
)

model.summary()

model.fit(x_train, y_train_onehot, epochs=5000, batch_size=50, callbacks=[callback], validation_data=(x_test, y_test_onehot))
model.save(model_name)
model.evaluate(x_test, y_test_onehot)
