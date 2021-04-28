import numpy as np

x = np.array([[1,2,3], [4,5,6]])
# [[1 2 3]
#  [4 5 6]]
v = np.array([1, 0, 1])
# [1 0 1]
y = np.empty_like(x)
# [[0 0 0]
#  [0 0 0]]

for i in range(len(x)):
    y[i, :] = x[i, :] + v
print(y)
# [[2 2 4]
#  [5 5 7]]

v2 = np.tile(v, (2, 1))
print(v2)
# [[1 0 1]
#  [1 0 1]]
print(x+v2)
# [[2 2 4]
#  [5 5 7]]

print(x+v)
# [[2 2 4]
#  [5 5 7]]

print(np.append(x,v))
# [1 2 3 4 5 6 1 0 1]

print(np.concatenate((x,[v])))
# [[1 2 3]
#  [4 5 6]
#  [1 0 1]]