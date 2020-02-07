import numpy as np
import pickle


# choose dimension of square
dim = 3;

test = np.random.randint(2, size=(dim,dim))
with open('test.pkl', 'wb') as outfile:
   pickle.dump(test, outfile)
