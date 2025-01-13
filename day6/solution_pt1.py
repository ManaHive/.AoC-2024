import time
import numpy as np

DAY = 6
with open(f'day{DAY}/input.txt') as i:
    input_nl = i.readlines()
input = np.array([list(l.strip('\n\r')) for l in input_nl])
with open(f'day{DAY}/test_input.txt') as i:
    test_nl = i.readlines()
test= np.array([list(l.strip('\n\r')) for l in test_nl])

curr = test.copy()
start_time = time.time()
#----------------------------------------
# PART 1: Input is a big ol' map, guard buddy is represented with ^
# they are constantly moving up until she sees an obstruction (#)
# if they see obstruction, they turn 90 degrees right
# 

def test_map(map):
    # List for directions, up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows = map.shape[0]
    cols = map.shape[1]

    lst_visited_spots = []
    facing = directions[0] # start by facing up
    dir_idx = 0
    guard_pos = np.where(map == '^')
    guard_row, guard_col = guard_pos[0][0], guard_pos[1][0]
    while(True):
        # if out of bounds, break
        if not (0 <= guard_row + facing[0] < rows and 0 <= guard_col + facing[1] < cols):
            if (guard_row, guard_col) not in lst_visited_spots:
                lst_visited_spots.append((guard_row,guard_col))
            map[guard_row][guard_col] = "X"
            break
        # check if there is obstruction based on facing direction, keep turning right until there is no obstruction in front:
        while(map[guard_row + facing[0]][guard_col + facing[1]] == '#'):
            # turn right
            dir_idx += 1
            facing = directions[dir_idx % 4]
        # for part 2: stored visited spots
        if (guard_row, guard_col) not in lst_visited_spots:
            lst_visited_spots.append((guard_row,guard_col))
        # move guard based on direction faced
        map[guard_row][guard_col], map[guard_row + facing[0]][guard_col + facing[1]] = "X", "^"
        # update guard_row, guard_col
        guard_row = guard_row + facing[0]
        guard_col = guard_col + facing[1]
    print(map)
    return lst_visited_spots
# part 1: test current map
part_one = test_map(curr)

print(f"Number of unique places visited: {len(part_one)}")
print(f"Execution time: {time.time() - start_time} seconds")