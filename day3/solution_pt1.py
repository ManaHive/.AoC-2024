import time
import numpy as np
import re

DAY = 3
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
# Input consists of garbled up text, must extract "mul(#,#)" from the text and multiply the two numbers, then add the sum

# regex can suck my cock
sum = 0
for l in curr:
    lst_mult = re.findall("mul\(\d?\d?\d?,\d?\d?\d?\)", l)
    for m in lst_mult:
        #print(m)
        sum += np.prod(np.array(re.split(",",m.strip("mul(,)")),dtype=int))

print(f"Sum: {sum}")
print(f"Execution time: {time.time() - start_time} seconds")