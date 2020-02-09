import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# import tensorflow as tf

data = pickle.load(open("data.pkl", 'rb'))

x1 = data[0]
x2 = data[1]
y = data[2]

X = np.concatenate((x1, x2), axis=1)

X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=7)
# print(data.head())

print(y)

print(x1[3])
print(x2[3])
print(y[3])

