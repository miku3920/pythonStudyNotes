import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

bool_idx = (a % 2) == 0
print(bool_idx)
# [[False  True False  True]
#  [False  True False  True]
#  [False  True False  True]]
print(a[bool_idx])
# [ 2  4  6  8 10 12]
print(a[a > 10])
# [11 12]
print(a[a % 2 == 1]*10)
# [ 10  30  50  70  90 110]
print(a[np.logical_and(a > 10, a % 2 == 0)])
# [12]
