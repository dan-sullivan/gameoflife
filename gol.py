import random
from os import system

w, h = 40, 40

universe = [[ bool(random.getrandbits(1)) for x in range(w)] for y in range(h)]

while True:
    system('clear')

    for y in range(h):
        for x in range(w):
            # Neighbour_coords n,ne,e,se,s,sw,w,nw
            neighbour_coords = [(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x+1,y-1),(x-1,y),(x-1,y-1)] 
            neighbour_count = 0
            # Get count of live neighbours
            for nx, ny in neighbour_coords:
                # Are we overstepping the bounds of our universe?
                if nx not in [-1,w] and ny not in [-1,h]:
                    neighbour_count += int(universe[nx][ny])
            # Are we alive or dead?
            if universe[x][y]:
            # Live cell
                # Underpopulation and overpopulation = death :(
                # 2 or 3 = lives on (we're already True)
                if neighbour_count < 2 or neighbour_count > 3:
                    universe[x][y] = False
            else:
            # Dead Cell
                # Reproduction
                if neighbour_count == 3:
                    universe[x][y] = True
        print "".join(["x" if c else " " for c in universe[y]])

