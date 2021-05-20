import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import tensorflow as tf

print(tf.__version__)
# python 3.8.3
# tensorflow 2.3.1
# gpu 1060 3GB
# CUDA 10.1
# cuDNN v8.0.4

hello = tf.constant('Hello, TensorFlow!')
print(hello)

hello = tf.config.experimental.list_physical_devices('GPU')
print(hello)
