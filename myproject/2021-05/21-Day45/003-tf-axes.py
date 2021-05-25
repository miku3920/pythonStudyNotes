import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

x1 = np.random.random((100, 2)) * -4 - 1
x2 = (np.random.random((100, 2)) * -4 - 1) + np.array([0, 6])
x3 = np.random.random((100, 2)) * 4 + 1
x4 = (np.random.random((100, 2)) * 4 + 1) - np.array([0, 6])
x_train = np.concatenate((x1, x2, x3, x4))

y1 = np.zeros((100,), dtype=int)
y2 = np.ones((100,), dtype=int)
y_train = np.concatenate((y1, y1, y2, y2))

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=1, activation=tf.nn.tanh, input_dim=2),
    tf.keras.layers.Dense(units=2, activation=tf.nn.softmax)
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x_train, y_train, epochs=200, batch_size=10)
model.summary()


weights, biases = model.layers[0].get_weights()
print(weights)
print(biases)


delta = 0.05
plt_x1 = np.arange(-6, 6, delta)
plt_x2 = np.arange(-6, 6, delta)
X, Y = np.meshgrid(plt_x1, plt_x2)
x = np.append(X, Y).reshape((2, -1)).transpose()
print(x.shape)
print(X.shape)
Z = model.predict(x)[:, 1].reshape((240, 240))

fig, ax = plt.subplots()
im = ax.imshow(
    Z, interpolation='bilinear', origin='lower',
    cmap="seismic", extent=(-6, 6, -6, 6)
)

levels = np.arange(-0.2, 1.2, 0.1)
CS = ax.contour(
    Z, levels, origin='lower', cmap='bwr',
    linewidths=2, extent=(-6, 6, -6, 6)
)
zc = CS.collections[6]
plt.setp(zc, linewidth=4)

ax.clabel(CS, levels, inline=1, fmt='% 1.1f',
          fontsize=14)

x_p = np.concatenate((x3, x4))
x_n = np.concatenate((x1, x2))
plt.plot(x_p[:, 0], x_p[:, 1], 'r.')
plt.plot(x_n[:, 0], x_n[:, 1], 'b.')
ax.set_title('matplotlib.axes.Axes.contour() Example')
plt.show()
