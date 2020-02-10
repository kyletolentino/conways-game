import numpy as np
import pickle
import argparse
# this is my functions.py module
import functions as func

# load input and display it
ex = pickle.load(open("input.pkl", 'rb'))
print("")
print(ex)

# run python gen.py n, where n = # of generations to pass
# default is n = 1 (i.e. one step)
parser = argparse.ArgumentParser(description='How many generations?', epilog='Hello there ;)')
parser.add_argument('gens', type=int, nargs='?', const=1, help = "Will run Conway's Game of Life for n generations", default=1)
args = parser.parse_args()

n = args.gens

# run the output
output = func.runs(ex, n)

print(output)
print("")
print("Created output.pkl")
print("")

# save the output
with open('output.pkl', 'wb') as outfile:
   pickle.dump(output, outfile)
