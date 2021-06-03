import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from tensorflow import keras
from keras import Model, layers, initializers
from keras.models import Sequential
import keras.backend as K
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


def myfunc(x):
    y = K.reshape(K.max(K.abs(x), axis=1) > 1, (-1, 1))
    return K.switch(K.concatenate([y, y, y]), x, K.zeros_like(x))


def x_tanh(x):
    return x - K.tanh(x)


def tanh2_tanh(x):
    return K.tanh(2 * x) - K.tanh(x)


def clip(x):
    return K.clip(x, -1, 1)


def clip_x(x):
    return K.clip(x, -1, 1) + 0.01 * x


def leaky_relu(x):
    return K.relu(x) + 0.01 * x


def swish(x):
    return 1.67653251702 * x * K.sigmoid(x)


def muti_relu(x):
    return K.concatenate([leaky_relu(x), leaky_relu(-x)])


def muti_swish(x):
    return K.concatenate([swish(x), swish(-x)])


model = Sequential()
model.add(layers.Dense(3, input_dim=2))
for i in range(50):
    model.add(layers.Dense(100))
    model.add(layers.Activation(swish))
model.add(layers.Dense(1))

model.compile(
    optimizer='adam',
    loss='hinge',
    metrics=['accuracy']
)

# model.fit(x_train, y_train, epochs=400, batch_size=20)
# model.summary()


def np_sigmoid(x):
    x = np.clip(x, -88.72, 88.72)
    return 1 / (1 + np.exp(-x))


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
    Z = np_sigmoid(model.predict(x)).reshape((240, 240))

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

for step in range(150):
    cost = model.train_on_batch(x_train, y_train)
    if step % 1 == 0:
        print(step, cost)
        plot()

plt.show()


def getLayerOutput(i, data):
    myModel = Model(
        inputs=model.input,
        outputs=model.layers[i].output
    )
    return myModel.predict(data)


def appendColumn(data):
    shape = data.shape[0]
    column = np.zeros((shape, 1))
    return np.append(data, column, axis=1)


def createFrame(input, output, frame=100):
    if(input.shape[1] == 1):
        input = appendColumn(input)

    if(output.shape[1] == 1):
        output = appendColumn(output)

    if(input.shape[1] == 2):
        input = appendColumn(input)

    if(output.shape[1] == 2):
        output = appendColumn(output)

    if(input.shape[1] > 3):
        input = input[:, :3]

    if(output.shape[1] > 3):
        output = output[:, :3]

    data = np.linspace((1, 2, 3), (10, 20, 30), frame).reshape((frame, 1, 3))
    for i, o in zip(input, output):
        unit = np.linspace(i, o, frame).reshape((frame, 1, 3))
        data = np.concatenate((data, unit), axis=1)
    return data[:, 1:, :]


def getData(x):
    data = np.zeros((1, x.shape[0], 3))
    upper_layer = x

    frame = createFrame(upper_layer, upper_layer, 10)
    data = np.concatenate((data, frame), axis=0)

    for i in range(len(model.layers)):
        layer = getLayerOutput(i, x)

        frame = createFrame(upper_layer, layer)
        data = np.concatenate((data, frame), axis=0)

        frame = createFrame(layer, layer, 10)
        data = np.concatenate((data, frame), axis=0)

        upper_layer = layer

    return data[1:, :, :]


def update(i, data, p_dots, n_dots):
    half = data.shape[1] // 2
    p_dots.set_data(data[i, half:, :2].transpose())
    p_dots.set_3d_properties(data[i, half:, 2])
    n_dots.set_data(data[i, :half, :2].transpose())
    n_dots.set_3d_properties(data[i, :half, 2])
    return data


fig = plt.figure()
ax = p3.Axes3D(fig)

ax.plot([-10, 10], [0, 0], [0, 0], 'r-', linewidth=0.3)
ax.plot([0, 0], [-10, 10], [0, 0], 'g-', linewidth=0.3)
ax.plot([0, 0], [0, 0], [-10, 10], 'b-', linewidth=0.3)

data = getData(x_train)
# 幀, 點, 座標

half = data.shape[1] // 2
p_dots = ax.plot(data[0, half:, 0], data[0, half:, 1], data[0, half:, 2], 'r.')[0]
n_dots = ax.plot(data[0, :half, 0], data[0, :half, 1], data[0, :half, 2], 'b.')[0]

# Setting the axes properties
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')
ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')
ax.set_zlim3d([-5.0, 5.0])
ax.set_zlabel('Z')
ax.set_title('xor by miku3920')

# Creating the Animation object
line_ani = animation.FuncAnimation(
    fig, update, data.shape[0],
    fargs=(data, p_dots, n_dots), interval=10, blit=False
)

plt.show()
