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
# PART 2:
# Check for do() and don't(), most recent instruction determines whether a mult command goes through or not

# regex can suck my cock
sum = 0
flag = True
for l in curr:
    lst_mult_pt2 = re.findall("do\(\)|don't\(\)|mul\(\d?\d?\d?,\d?\d?\d?\)", l)
    for m in lst_mult_pt2:
        if m == "do()":
            flag = True
        elif m == "don't()":
            flag = False
        else:
            sum += np.prod(np.array(re.split(",",m.strip("mul(,)")),dtype=int)) if flag else 0
        #print(m)
        
print(f"Sum: {sum}")
print(f"Execution time: {time.time() - start_time} seconds")