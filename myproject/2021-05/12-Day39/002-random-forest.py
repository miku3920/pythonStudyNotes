from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier
import numpy as np

x = np.array([
    [180, 85], [174, 80], [170, 75],
    [167, 45], [158, 52], [155, 44]
])
y = np.array([
    'man', 'man', 'man',
    'woman', 'woman',  'woman'
])

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=2
).fit(x, y)

print(model.predict([[180, 85]]))

export_graphviz(model.estimators_[5], out_file='tree.dot')
