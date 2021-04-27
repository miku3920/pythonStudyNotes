import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(a)
# [1 2 3]
print(type(a))
# <type 'numpy.ndarray'>
print(a.shape)
# (3,)
print(a[0], a[1], a[2])
# 1 2 3
a[0] = 5
print(a)
# [5, 2, 3]
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)
# (2, 3)
print(b[0, 0], b[0, 1], b[1, 0])
# 1 2 4
print(b[0:2, 1:3])
# [[2 3]
#  [5 6]]
print(b[[0,0], [2,1]])
# [3 2] 
# [b[0,2] b[0,1]]
c = np.reshape(b,(3,2))
print(c)
# [[1 2]
#  [3 4]
#  [5 6]]
d = np.reshape(b,(-1,))
print(d)
# [1 2 3 4 5 6]