import time
import numpy as np

DAY = 9
with open(f'day{DAY}/input.txt') as i:
    input_nl = i.readlines()
input = np.array([l.strip('\n\r') for l in input_nl])
with open(f'day{DAY}/test_input.txt') as i:
    test_nl = i.readlines()
test= np.array([l.strip('\n\r') for l in test_nl])
curr = input.copy()
start_time = time.time()
#----------------------------------------
# PART 1:

print(f"Execution time: {time.time() - start_time} seconds")