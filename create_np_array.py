import numpy as np
import functions as func
import random
import pickle

# x1 and x2 are feature vectors, i.e. first matrix and sequential matrix
# y will be labels
x1 = []
x2 = []
y = []

# generate 200000 samples (the more the merrier!)
# NOTE: I only ran this once because the it would generate random data each time it runs
for i in range(200000):
    pick = random.randint(0, 1)
    state = np.random.randint(2, size=(3, 3))

    # if pick is 0, create fake step, w/ label 0
    if (pick == 0):
        x1.append(state)
        x2.append(func.false_step(state))
        y.append(0)
    # if pick is 1, create real step, w/ label 1
    else:
        x1.append(state)
        x2.append(func.step(state))
        y.append(1)

# store each array into another list
data = [x1, x2, y]

# save as data
with open('data.pkl', 'wb') as outfile:
    pickle.dump(data, outfile)
