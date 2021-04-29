import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

x_values = pd.DataFrame([0, 1, 2, 3, 4, 5])
y_values = pd.DataFrame([0.1, 0.5, 0.7, 0.8, 1.2, 1.3])
x_test = pd.DataFrame([1.5, 3, 5])

body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

y_test_predict = body_reg.predict(x_test)
print(y_test_predict)
# [[0.53238095]
#  [0.88380952]
#  [1.35238095]]

line_x = [x_values.min(), x_values.max()]
line_y = list(body_reg.predict(pd.DataFrame(line_x)))
plt.plot(line_x, line_y, 'r--')
plt.scatter(x_values, y_values)
plt.scatter(x_test, y_test_predict, color='red')
plt.show()
