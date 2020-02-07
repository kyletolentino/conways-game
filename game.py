import numpy as np
import pickle

# calling my functions
# import functions.py as func

# ex = pickle.load(open("test.pkl", 'rb'))
ex = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
temp = ex

print(ex)

for x in range(ex.shape[0]):
    for y in range(ex.shape[1]):

        # corner case
        if ((x==0 or x==ex.shape[0]-1) and (y==0 or y==ex.shape[1]-1)):
            print("Corner: ", ex[x][y])

        # side case
        elif ((x==0 or x==ex.shape[0]-1) or (y==0 or y==ex.shape[1]-1)):
            print("Side: ", ex[x][y])

        # everything else
        else:
            print("Else: ", ex[x][y])