import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np

sample = 100
x1 = np.random.random((sample, 2)) * -4 - 0.2
x2 = np.random.random((sample, 2)) * 4 + 0.2
x3 = (np.random.random((sample, 2)) * -4 - 0.2) + np.array([0, 4.4])
x4 = (np.random.random((sample, 2)) * 4 + 0.2) - np.array([0, 4.4])
x_train = np.concatenate((x1, x2, x3, x4))

y1 = np.zeros((sample,), dtype=int)
y2 = np.ones((sample,), dtype=int)
y_train = np.concatenate((y1, y1, y2, y2))

model = Sequential([
    layers.Dense(3, input_dim=2),
    layers.Activation('relu'),
    layers.Dense(2),
    layers.Activation('softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


delta = 0.05
plt_x1 = np.arange(-6, 6, delta)
plt_x2 = np.arange(-6, 6, delta)
X, Y = np.meshgrid(plt_x1, plt_x2)
x = np.append(X, Y).reshape((2, -1)).transpose()
x_p = np.concatenate((x3, x4))
x_n = np.concatenate((x1, x2))

fig, ax = plt.subplots()
levels = np.arange(-0.2, 1.2, 0.1)
ax.set_title('axes by miku3920')

def plot(sleep=1e-8):
    plt.cla()
    Z = model.predict(x)[:, 1].reshape((240, 240))

    im = ax.imshow(
        Z, interpolation='bilinear', origin='lower',
        cmap="seismic", extent=(-6, 6, -6, 6)
    )

    CS = ax.contour(
        Z, levels, origin='lower', cmap='bwr',
        linewidths=2, extent=(-6, 6, -6, 6)
    )
    zc = CS.collections[6]
    plt.setp(zc, linewidth=2)

    ax.clabel(CS, levels, inline=1, fmt='% 1.1f',
              fontsize=14)

    ax.set_title('axes by miku3920')
    plt.plot(x_p[:, 0], x_p[:, 1], 'r.')
    plt.plot(x_n[:, 0], x_n[:, 1], 'b.')
    plt.pause(sleep)

plot(5)

for step in range(10000):
    cost = model.train_on_batch(x_train, y_train)
    if step % 100 == 0:
        print(step, cost)
        plot()

plt.show()
