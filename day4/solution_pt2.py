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
# PART 2:
# Gotta find X-Mases, 2 MAS in an X shape
print(curr)
print(curr.shape)

# Dictionary for diagonals
diagonals = {
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
    # check bounds, only checking diagonals
    if x == "A" and 1 <= idx[0] < rows - 1 and 1 <= idx[1] < cols - 1:
        lst_diag = []
        # get values from all diagonals, then check if combination is valid for X-MAS
        for d, (row_offset, col_offset) in diagonals.items():
            lst_diag.append(str(curr[idx[0]+row_offset,idx[1]+col_offset]))
        # all possible combinations of X-MAS, ["MSMS"],["MMSS"],["SMSM"],["SSMM"]
        if lst_diag in [["M","S","M","S"], ["M","M","S","S"], ["S","M","S","M"], ["S","S","M","M"]]:
            lst_xmas.append((idx,lst_diag))

print(f"List of X-MAS: {lst_xmas}")
print(f"Found: {len(lst_xmas)}")
print(f"Execution time: {time.time() - start_time} seconds")