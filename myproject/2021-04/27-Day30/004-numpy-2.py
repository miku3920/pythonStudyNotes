import numpy as np

a = np.zeros((2, 2))
print(a)
# [[0. 0.]
#  [0. 0.]]
b = np.ones((1, 2))
print(b)
# [[1. 1.]]
c = np.full((2, 2), 7)
print(c)
# [[7 7]
#  [7 7]]
d = np.eye(3)
print(d)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
e = np.random.random((2, 2))
print(e)
# [[0.32152571 0.66176581]
#  [0.22736177 0.69021088]]
