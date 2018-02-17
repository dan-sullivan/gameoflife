import random
from os import system

w, h = 80, 25
c_char = "o"

universe = [[ bool(random.getrandbits(1)) for x in range(w)] for y in range(h)]

while True:

    # Set up a frame to write to in memory before screen for visual performance
    universe_frame = ""
    for y in range(h):
        for x in range(w):
            # Neighbour_coords n,ne,e,se,s,sw,w,nw
            neighbour_coords = [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x+1,y-1),(x-1,y),(x-1,y-1)] 
            neighbour_count = 0
            # Get count of live neighbours
            for nx, ny in neighbour_coords:
                # Are we overstepping the bounds of our universe?
                if nx not in [-1,w] and ny not in [-1,h]:
                    neighbour_count += int(universe[ny][nx])
            # Are we alive or dead?
            if universe[y][x]:
            # Live cell
                # Underpopulation and overpopulation = death :(
                # 2 or 3 = lives on (we're already True)
                if neighbour_count < 2 or neighbour_count > 3:
                    universe[y][x] = False
            else:
            # Dead Cell
                # Reproduction
                if neighbour_count == 3:
                    universe[y][x] = True
        # Add row to universe frame
        universe_frame += "".join([c_char if c else " " for c in universe[y]]) + "\n"
    # Print frame
    system('clear')
    print universe_frame
