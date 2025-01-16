import time
import numpy as np
import itertools

DAY = 8
with open(f'day{DAY}/input.txt') as i:
    input_nl = i.readlines()
input = np.array([list(l.strip('\n\r')) for l in input_nl])
with open(f'day{DAY}/test_input.txt') as i:
    test_nl = i.readlines()
test= np.array([list(l.strip('\n\r')) for l in test_nl])
curr = input.copy()
start_time = time.time()
#----------------------------------------
# PART 1: Gotta find all the antinodes for each frequency (every set of letters/digits on the map), for every pair of same frequency antenna nodes, an antinode is double the distance away from this pair
# Antinodes can overlap with existing antenna spaces
# GOAL: Find all unique antinode spots
# PART 2: There can be many antinodes for a pair, as long as they are inline
antenna_map = curr.copy()
rows = antenna_map.shape[0]
cols = antenna_map.shape[1]

marked_map = antenna_map.copy()
lst_frequency = np.unique(antenna_map)
print(lst_frequency)
lst_antenna = []
lst_overlap = []
for fq in lst_frequency:
    if fq != ".":
        positions = np.where(antenna_map == fq)
        pos_zip = zip(positions[0], positions[1])
        pairs = itertools.combinations(pos_zip, 2)
        for p in pairs:
            distance = (p[1][0] - p[0][0],p[1][1]-p[0][1])
            antinodes = []
            r, c = p[0][0], p[0][1]
            antinodes.append((r,c))
            # forward
            while (0 <= r < rows and 0 <= c < cols):
                r += distance[0]
                c += distance[1]
                antinodes.append((r, c))
            # back
            r, c = p[0][0], p[0][1]
            while (0 <= r < rows and 0 <= c < cols):
                r -= distance[0]
                c -= distance[1]
                antinodes.append((r, c))
            for a in antinodes:
                row = a[0]
                col = a[1]
                if not(0 <= row < rows and 0 <= col < cols) or (row,col) in lst_antenna:
                    continue
                else:
                    if antenna_map[row][col] == ".":
                        marked_map[row][col] = "#"
                    else:
                        lst_overlap.append((row,col))
                    lst_antenna.append((row,col))

print(marked_map)
print(f"Number of unique antinodes: {len(lst_antenna)}")
print(np.count_nonzero(marked_map == "#"))
print(len(lst_overlap))
print(f"Execution time: {time.time() - start_time} seconds")