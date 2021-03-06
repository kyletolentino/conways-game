import numpy as np
import pickle
import argparse

# NOTE: if you want to generate n x m numpy arrays instead of m x m,
#  edit input line to be size = (dim, h)

# will let gen.py take arguments for dim
# if only one argument, grid will be square
# if 2 arguments, grid will be w xinput = np.random.randint(2, size=(dim,dim))
parser = argparse.ArgumentParser(description="Choose dimension of grid")
parser.add_argument('length', const=3, nargs='?',type=int, default=3)
parser.add_argument('height', const=3, nargs='?', type=int, default=3)
args = parser.parse_args()

# choose dimension of square
dim = args.length

# can also choose a non-square shape
# *must change (dim, dim) to (w,h) within 'input'
h = args.height


# create a random numpy array with values of 0s and 1s
input = np.random.randint(2, size=(dim, dim))

# print input to see if you like, if not then run gen.py again
print(input)

with open('input.pkl', 'wb') as outfile:
   pickle.dump(input, outfile)

print("")
print("Created input.pkl")
