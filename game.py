import numpy as np
import pickle

# ex = np.array([[0, 1, 3], [4, 5, 6], [7, 8, 9]])
ex = pickle.load(open("test.pkl", 'rb'))
temp = ex

print("Original \n")
print(ex)


for x in range(ex.shape[0]):
    for y in range(ex.shape[1]):
        # corner case
        if ((x==0 or x==ex.shape[0]-1) and (y==0 or y==ex.shape[1]-1)):
            print(temp[x][y])