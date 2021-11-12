import copy, random, sys, time

WIDTH = 79  # The width of the cell grid.
HEIGHT = 20     # The height of the cell grid.

ALIVE = 'O'     # The character representing a living cell.
DEAD = ' '  # The character representing a dead cell.

# The cells and nextCells are dictionaries for the state of the game
# Their keys are (x, y) tuples and their values are one of the ALIVE or DEAD values.
nextCells = {}

# Put random dead and alive cells into nextCells:
for x in range(WIDTH):  # loop over every possible column.
    for y in range(HEIGHT):     # loop over every possible row
        if random.randint(0, 1) == 0:   # 50/50 chance for starting cells being alive or dead.
            nextCells[(x, y)] = ALIVE   # Add a living cell
        else:
            nextCells[(x, y)] = DEAD    # Add a dead cell
while True:
    # Each iteration of this loop is a step of the simulation
    print('\n' * 50)
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit.')

    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Get the neighboring coordinates of (x, y) even if they wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # count the number of living neighbors:
            num_neighbors = 0
            if cells[(left, above)] == ALIVE:
                num_neighbors += 1  # top left neighbor is alive
            if cells[(x, above)] == ALIVE:
                num_neighbors += 1  # top neighbor is alive
            if cells[(right, above)] == ALIVE:
                num_neighbors += 1  # top right neighbor is alive
            if cells[(left, y)] == ALIVE:
                num_neighbors += 1  # left neighbor is alive
            if cells[(right, y)] == ALIVE:
                num_neighbors += 1  # right neighbor is alive
            if cells[(left, below)] == ALIVE:
                num_neighbors += 1  # left below neighbor is alive
            if cells[(x, below)] == ALIVE:
                num_neighbors += 1  # below neighbor is alive
            if cells[(right, below)] == ALIVE:
                num_neighbors += 1  # below right neighbor is alive

            # set cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (num_neighbors == 2 or num_neighbors == 3):
                # neighboring cells with two or three neighbors stay alive:
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and num_neighbors == 3:
                nextCells[(x, y)] = ALIVE
            else:
                # everything else dies or stays dead:
                nextCells[(x, y)] = DEAD
    try:
        time.sleep(1) # Add a one second pause to reduce flickering
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()