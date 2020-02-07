import numpy as np
import pickle

# calling my functions
import functions as func

ex = pickle.load(open("test.pkl", 'rb'))
# first = np.array([[0,1,0], [0,1,1], [1,0,1]])

# need to create temporary state before looping
# don't want to access edited values while iterating
# i.e. something changed in row 1, but row 2 needs original value

next = np.zeros((ex.shape[0], ex.shape[1]), dtype=int)

print(ex)
print("")


for x in range(ex.shape[0]):
    for y in range(ex.shape[1]):

        next[x][y] = func.check((x,y), ex)

print(next)