import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
print(np.shape(diabetes.data))

x = diabetes.data[:, np.newaxis, 2]

x_train = x[:-20]
y_train = diabetes.target[:-20]
x_test = x[-20:]
y_test = diabetes.target[-20:]

print(np.shape(x_train))
print(np.shape(y_train))
print(np.shape(x_test))
print(np.shape(y_test))

body_reg = linear_model.LinearRegression()
body_reg.fit(x_train, y_train)

line_x = [x_train.min(), x_train.max()]
line_y = list(body_reg.predict(pd.DataFrame(line_x)))
plt.plot(line_x, line_y, 'r--')
plt.scatter(x_train, y_train,  color='black')
plt.scatter(x_test, y_test,  color='red')
plt.show()