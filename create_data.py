import numpy as np
import functions as func
import csv
import random

with open('data.csv','w') as f:
    writer=csv.writer(f, delimiter=',',lineterminator='\n',)
    writer.writerow(["Matrix 1", "Matrix 2", "Target"])
    for i in range(5):
        # randomly adds real/fake data
        pick = random.randint(0,1)
        if (pick == 0):
            writer.writerow(func.gen_false())
        else:
            writer.writerow(func.gen_real())
