import numpy as np

# RULES:
# Any dead cell with 3 live neighbors (in the 3x3 grid centered on that cell) becomes filled
# Any live cell with 2 or 3 live neighbors stays live
# All other cells die or stay dead


# General Strat:
# for each function, it takes the position and state/generation (i.e. the matrix)
# if out of bounds, continue
# count up all 1s w/in perimeter of (x,y)


def check(position, state):
    # position will be tuple (x,y)
    x = position[0]
    y = position[1]
    count = 0

    # created two for loops to get # of 1s around given position
    # if i,j go out of bounds, just skip to next iteration w/ continue
    for i in range(x-1, x+2):
        if (i<0 or i>state.shape[0]-1):
            continue
        for j in range(y-1, y+2):
            if (j<0 or j>state.shape[1]-1):
                continue

            # need to prevent cell from counting itself (in case it was 1)
            if(i == x and j == y):
                continue

            # count up all 1s surrounding cell
            if (state[i][j] == 1):
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


def step(state):
    # need to create temporary state (next) before looping
    # don't want to access edited values while iterating
    # i.e. something changed in row 1, but row 2 needs original value
    next = np.zeros((state.shape[0], state.shape[1]), dtype=int)

    for x in range(state.shape[0]):
        for y in range(state.shape[1]):
            # run check function to step
            next[x][y] = check((x,y), state)

    return next
