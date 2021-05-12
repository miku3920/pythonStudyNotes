from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import numpy as np

x = np.array([
    # 柳丁
    # 寬, 高
    [9.0, 9.0],
    [9.2, 9.2],
    [9.6, 9.2],
    [9.2, 9.2],
    [6.7, 7.1],
    [7.0, 7.4],
    [7.6, 7.5],
    # 檸檬
    [7.2, 10.3],
    [7.3, 10.5],
    [7.2, 9.2],
    [7.3, 10.2],
    [7.2, 9.7],
    [7.3, 10.1],
    [7.3, 10.1]
])
y = np.array([
    0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1
])

x_test = np.array([[8, 8], [8.3, 8.3]])

model = GaussianNB().fit(x, y)
print(model.class_prior_)
print(model.get_params())

predicted = model.predict(x_test)
print(predicted)
print(model.predict_proba(x_test))

plt.plot(x[:7, :1], x[:7, -1:], 'b.')
plt.plot(x[7:, :1], x[7:, -1:], 'g.')
plt.plot(x_test[:,1], x_test[:,-1:], 'r.')

plt.axis([6, 11, 6, 11])
plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange', 'Lemons'), loc='upper right')
plt.show()