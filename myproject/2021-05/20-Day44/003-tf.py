import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

x1 = np.random.random((500, 1))
x2 = np.random.random((500, 1)) + 1
x = np.concatenate((x1, x2))

y1 = np.zeros((500,), dtype=int)
y2 = np.ones((500,), dtype=int)
y = np.concatenate((y1, y2))

print(x.shape)
print(y.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation=tf.nn.relu, input_dim=1),
    tf.keras.layers.Dense(2, activation=tf.nn.relu),
    tf.keras.layers.Dense(2, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x, y, epochs=20, batch_size=10)
print(tf.keras.utils.model_to_dot(model).to_string())
tf.keras.utils.plot_model(model, show_shapes=True, show_layer_names=False)
plt.plot(x1, y1, 'b.')
plt.plot(x2, y2, 'g.')
plt.show()
