import numpy as np
import pickle

ex = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])

for i in range(ex.shape[0]):
    for j in range(ex.shape[1]):
        print(ex[i][j])
