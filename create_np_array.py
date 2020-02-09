import numpy as np
import functions as func
import random
import pickle

x1 = []
x2 = []
y = []

for i in range(200000):
    pick = random.randint(0, 1)
    state = np.random.randint(2, size=(3, 3))

    # if pick is 0, create fake step, else make it real
    if (pick == 0):
        x1.append(state)
        x2.append(func.false_step(state))
        y.append(0)
    else:
        x1.append(state)
        x2.append(func.step(state))
        y.append(1)

data = [x1, x2, y]

with open('data.pkl', 'wb') as outfile:
    pickle.dump(data, outfile)
