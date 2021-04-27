import numpy as np
a=np.array([1,2])
print(a.dtype)
# int32
b=np.array([1.0,2.0])
print(b.dtype)
# float64
c=np.array([1,2],dtype=np.float64)
print(c.dtype)
# float64
d=np.array(c,dtype=np.int64)
print(d.dtype)
# int64