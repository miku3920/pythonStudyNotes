import numpy as np

x = np.array([[-1,2,3],[13,14,15]])
print(x)
# [[-1  2  3] 
#  [13 14 15]]
print(x.sum())
print(np.sum(x))
# 46
print(np.sum(x, axis=0))  
# [12 16 18]
print(np.sum(x, axis=1))  
# [4 42]
print(np.max(x))       
# 15
print(np.min(x))       
# -1
print(np.cumsum(x))    
# [-1  1  4 17 31 46]
print(np.average(x))
print(np.mean(x))
# 7.666666666666667
print(np.median(x))
# 8.0
print(np.std(x)) # 標準差
# 6.472162612982533
# std = sqrt(mean(abs(x - x.mean())**2))
print(np.var(x)) # 變異數
# 41.88888888888889
# var = mean(abs(x - x.mean())**2)
print(x.T)
# [[-1 13]
#  [ 2 14]
#  [ 3 15]]