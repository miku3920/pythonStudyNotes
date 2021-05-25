import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import tensorflow as tf
from tensorflow.keras import Model
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

model.fit(x_train, y_train, epochs=1000, batch_size=10)
model.summary()


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


def createFrame(input, output, frame=500):
    if(input.shape[1] == 2):
        input = appendColumn(input)

    if(output.shape[1] == 2):
        output = appendColumn(output)

    data = np.linspace((1, 2, 3), (10, 20, 30), frame).reshape((frame, 1, 3))
    for i, o in zip(input, output):
        unit = np.linspace(i, o, frame).reshape((frame, 1, 3))
        data = np.concatenate((data, unit), axis=1)
    return data[:, 1:, :]


def getData(x):
    data = np.zeros((1, x.shape[0], 3))
    upper_layer = x

    frame = createFrame(upper_layer, upper_layer, 100)
    data = np.concatenate((data, frame), axis=0)

    for i in range(len(model.layers)):
        layer = getLayerOutput(i, x)

        frame = createFrame(upper_layer, layer)
        data = np.concatenate((data, frame), axis=0)

        frame = createFrame(layer, layer, 100)
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
ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(
    fig, update, data.shape[0],
    fargs=(data, p_dots, n_dots), interval=10, blit=False
)

plt.show()
