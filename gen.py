import numpy as np
import pickle

empty_grid = np.zeros((3,3))
with open('empty.pkl', 'wb') as outfile:
    pickle.dump(empty_grid, outfile)
