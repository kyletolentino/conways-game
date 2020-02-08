import numpy as np
import pickle
import argparse
# calling my functions
import functions as func

ex = pickle.load(open("input.pkl", 'rb'))
print("")
print(ex)

# run python gen.py n, where n = # of generations to pass
# default is n=1 (i.e. one step)
parser = argparse.ArgumentParser(description='How many generations?', epilog='Hello there ;)')
parser.add_argument('gens', type=int, nargs='?', const=1, help = "Will run Conway's Game of Life for n generations")
args = parser.parse_args()

n = args.gens

# if you just want to see the end state, delete the print statments inside runs()
def runs(state, n):
    count = n
    if count<=1:
        print("")
        print("    V")
        print("")
        return func.step(state)
    else:
        count -= 1
        next = func.step(state)
        print("")
        print("    V")
        print("")
        print(next)
        return runs(next, count)

output = runs(ex, n)
print(output)
print("")
print("Created output.pkl")
print("")

with open('output.pkl', 'wb') as outfile:
   pickle.dump(output, outfile)
