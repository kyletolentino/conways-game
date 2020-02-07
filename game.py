import numpy as np
import pickle
import argparse
# calling my functions
import functions as func

ex = pickle.load(open("input.pkl", 'rb'))
print("")
print(ex)

n = 4

def runs(state, n):
    count = n
    if count<=1:
        print("")
        #print("    |")
        print("    V")
        print("")
        return func.step(state)
    else:
        count -= 1
        next = func.step(state)
        print("")
        #print("    |")
        print("    V")
        print("")
        print(next)
        return runs(next, count)

print(runs(ex, n))
print("")
