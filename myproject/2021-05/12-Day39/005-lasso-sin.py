from sklearn.linear_model import Lasso
from sklearn.pipeline import make_pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import matplotlib.pyplot as plt
import numpy as np


class GaussianFeatures(BaseEstimator, TransformerMixin):
    """Uniformly spaced Gaussian features for one-dimensional input"""

    def __init__(self, N, width_factor=2.0):
        self.N = N
        self.width_factor = width_factor

    @staticmethod
    def _gauss_basis(x, y, width, axis=None):
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))

    def fit(self, X, y=None):
        # create N centers spread along the data range
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self

    def transform(self, X):
        return self._gauss_basis(
            X[:, :, np.newaxis],
            self.centers_,
            self.width_, axis=1
        )


x = np.arange(0, 720, 1).reshape(-1, 1)
y = np.sin(2 * np.pi * x / 180)+np.random.normal(0, 1e-1, len(x)).reshape(-1, 1)
x_test = np.arange(0, 1440, 1).reshape(-1, 1)

model = make_pipeline(
    GaussianFeatures(30),
    Lasso(alpha=1e-5)
).fit(x, y)
y_pred = model.predict(x_test)

plt.plot(x, y, 'k.')
plt.plot(x_test, y_pred, 'r-')
plt.show()
