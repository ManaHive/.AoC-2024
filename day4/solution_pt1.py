import time
import numpy as np

# turning the strings into list of chars in order to make 2D arrays
DAY = 4
with open(f'day{DAY}/input.txt') as i:
    input_nl = i.readlines()
input = np.array([list(l.strip('\n\r')) for l in input_nl])
with open(f'day{DAY}/test_input.txt') as i:
    test_nl = i.readlines()
test= np.array([list(l.strip('\n\r')) for l in test_nl])

curr = input.copy()
start_time = time.time()
#----------------------------------------
# PART 1:
# its a word searchhh, find all instances of XMAS in the word search, can be forwards, backwards, horizontal, vertical, diagonal, and overlapping other words
print(curr)
print(curr.shape)

# Dictionary for directions
directions = {
    'ahead': (0, 1),
    'behind': (0, -1),
    'above': (-1, 0),
    'below': (1, 0),
    'diagonal_top_left': (-1, -1),
    'diagonal_top_right': (-1, 1),
    'diagonal_bottom_left': (1, -1),
    'diagonal_bottom_right': (1, 1),
}
rows = curr.shape[0]
cols = curr.shape[1]
lst_xmas = []
successFlag = False
for idx, x in np.ndenumerate(curr):
    if x == "X":
        for direction, (row_offset, col_offset) in directions.items():
            successFlag = True
            new_row, new_col = idx[0], idx[1]
            for c in "MAS":
                new_row, new_col = new_row + row_offset, new_col + col_offset
                if not(0 <= new_row < rows and 0 <= new_col < cols):  # Check bounds
                    successFlag = False
                    break
                else:
                    #print(f"og: {idx} idx: {(new_row, new_col)} Curr: {curr[new_row, new_col]} direction: {direction}")
                    if curr[new_row,new_col] == c:
                        successFlag = True
                    else:
                        successFlag = False
                        break
            if successFlag:
                lst_xmas.append([idx, direction])

print(f"List of XMAS: {lst_xmas}")
print(f"Found: {len(lst_xmas)}")
print(f"Execution time: {time.time() - start_time} seconds")