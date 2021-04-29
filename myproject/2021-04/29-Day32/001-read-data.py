import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')
data = data.iloc[:, 1:]
# data[data == 'NR'] = 0
raw_data = data.to_numpy()
print(raw_data)