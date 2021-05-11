import numpy as np
from sklearn import tree

x = np.array([
    [180, 85], [174, 80], [170, 75],
    [167, 45], [158, 52], [155, 44]
])
y = np.array(['man', 'man', 'man', 'woman', 'woman',  'woman'])

clf = tree.DecisionTreeClassifier().fit(x, y)

tree.export_graphviz(clf, out_file='tree.dot')
