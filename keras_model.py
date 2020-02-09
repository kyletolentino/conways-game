import pandas as pd
import matplotlib.pyplot as plt
# import tensorflow as tf
from sklearn.model_selection import train_test_split

batch_size = 32
num_classes = 2
epochs = 12

# preprocessing data
data = pd.read_csv('./data.csv')

y = data['target'].values
X = data.drop('target', axis=1)

X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=7)

print(X_train.shape)
