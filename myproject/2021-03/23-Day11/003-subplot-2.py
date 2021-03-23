import matplotlib.pyplot as plt

t1=[1,2,3,4]
t2=[2,4,6,8]

plt.subplot(3,1,(1,2),facecolor='k')
plt.plot(t1, t2, 'g--')

plt.subplot(3,1,3)
plt.plot(t1, t2, 'b|')

plt.show()