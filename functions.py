import numpy as np

# RULES:
# Any dead cell with 3 live neighbors (in the 3x3 grid centered on that cell) becomes filled
# Any live cell with 2 or 3 live neighbors stays live
# All other cells die or stay dead


# General Strat:
# created functions for the 3 cases
# for each function, it takes the position and state/generation (i.e. the matrix)


def check(position, state):
    x = position[0]
    y = position[1]
    count = 0

    # created two for loops to get # of 1s around given position
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # needed this to prevent cell from counting itself (in case it was 1)
            if(i == x and j == y):
                continue
            elif (state[i][j] == 1):
                count += 1
    

    # apply rules if cell is dead/alive
    if (state[x][y] == 0):
        if (count == 3):
            return 1
        else:
            return 0
    else:
        if (count == 2 or count == 3):
            return 1
        else:
            return 0