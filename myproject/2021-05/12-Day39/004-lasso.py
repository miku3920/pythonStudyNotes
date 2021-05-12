from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

x = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]])
y = np.array([[0.1], [0.5], [0.7], [0.8], [1.2], [1.3]])
x_test = np.array([[1.5], [3.0], [5.0]])

model = linear_model.Lasso(alpha=0.1).fit(x, y)
y_pred = model.predict(x_test)
print(y_pred)

line_x = [[x.min()], [x.max()]]
line_y = model.predict(line_x)
plt.plot(line_x, line_y, 'k-')
plt.plot(x, y,'b.')
plt.plot(x_test, y_pred, 'r.')
plt.show()