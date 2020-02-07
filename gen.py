import numpy as np
import pickle

# empty_grid = np.zeros((3,3))
# with open('empty.pkl', 'wb') as outfile:
#    pickle.dump(empty_grid, outfile)


d = 3;

test = np.random.randint(2, size=(d,d))
with open('test.pkl', 'wb') as outfile:
   pickle.dump(test, outfile)
