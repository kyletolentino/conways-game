import numpy as np
import pickle

# calling my functions
import functions as func

ex = pickle.load(open("test.pkl", 'rb'))
display = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# need to create temporary state before looping
# don't want to access edited values while iterating
# i.e. something changed in row 1, but row 2 needs original value
temp = ex

print(ex)
print("")


for x in range(ex.shape[0]):
    for y in range(ex.shape[1]):

        # corner case
        if ((x==0 or x==ex.shape[0]-1) and (y==0 or y==ex.shape[1]-1)):
            ex[x][y] = func.check((x,y), temp)

        # side case
        elif ((x==0 or x==ex.shape[0]-1) or (y==0 or y==ex.shape[1]-1)):
            continue

        # everything else
        else:
            ex[x][y] = func.check((x,y), temp)

print(ex)