import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
v = np.array([9, 10], dtype=np.float64)

print(x + y)
print(np.add(x, y))
# [[ 6.  8.]
#  [10. 12.]]
print(x + 10)
# [[11. 12.] 
#  [13. 14.]]

print(x - y)
print(np.subtract(x, y))
# [[-4. -4.] 
#  [-4. -4.]]
print(x - [1, 2])
# [[0. 0.]
#  [2. 2.]]

print(x * y)
print(np.multiply(x, y))
# [[ 5. 12.]
#  [21. 32.]]

print(x / y)
print(np.divide(x, y))
# [[0.2        0.33333333]
#  [0.42857143 0.5       ]]

print(x ** 2)
# [[ 1.  4.]
#  [ 9. 16.]]

print(np.sqrt(x))
# [[1.         1.41421356]
#  [1.73205081 2.        ]]

print(x.dot(y))
print(np.dot(x, y))
# [[19. 22.]
#  [43. 50.]]
# 1*5 + 2*7 =  5+14   1*6 + 2*8 =  6+16
# 3*5 + 4*7 = 15+28   3*6 + 4*8 = 18+32
