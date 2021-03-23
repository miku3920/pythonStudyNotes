import numpy as np
import matplotlib.pyplot as plt

t1=[1,2,3,4]
t2=[2,4,6,8]

fig, axs = plt.subplots(2, 2)
axs[0][0].plot(t1, t2)
axs[1][1].plot(t1, t2)

plt.show()