import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# source: https://seaborn.pydata.org/generated/seaborn.pairplot.html

iris = sns.load_dataset('iris')
sns.pairplot(data=iris, kind='scatter', hue='species')
plt.show()
