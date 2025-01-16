import time
import numpy as np
import itertools
from copy import deepcopy

DAY = 9
with open(f'day{DAY}/input.txt') as i:
    input_nl = i.readlines()
input = input_nl[0]
with open(f'day{DAY}/test_input.txt') as i:
    test_nl = i.readlines()
test = test_nl[0]
curr = [int (i) for i in input]
start_time = time.time()
#----------------------------------------
# PART 1:
# GOAL: Find checksum of the files after sorting them
# Input consists of a single line of numbers, alternating from length of file > free space > length > free
# File blocks have an index starting at 0
# Checksum is index number of file block * left-most file block position
# Sorting = compacting files by grabbing files from the end of the line, and putting it in first available free space

file_blocks = curr[::2]
free_space = curr[1::2]
# print(f"Blocks: {file_blocks}")
# print(f"Free Space: {free_space}")

final_string = ""
idx = 0
reserve_stack = []
length_of_file_blocks = len(file_blocks)
length_of_final_string = sum(file_blocks)

for f in file_blocks:
    for b in itertools.repeat(idx, f):
        final_string += str(b)
        if len(final_string) >= length_of_final_string:
            break
    if idx < len(free_space) - 1:
        free_space_block_length = free_space[idx]
        step = 0
        while (free_space_block_length > 0 and len(final_string) < length_of_final_string):
            # check reserve stack first, then look at the back of file_blocks again
            if len(reserve_stack) != 0:
                for reserve in deepcopy(reserve_stack):
                    final_string += str(reserve)
                    reserve_stack.remove(reserve)
                    free_space_block_length -= 1
                    if free_space_block_length <= 0 or len(final_string) >= length_of_final_string:
                        break
                if free_space_block_length <= 0 or len(final_string) >= length_of_final_string:
                    break
            reverse_b_idx = length_of_file_blocks-idx-step-1
            reverse_b = file_blocks[reverse_b_idx]
            num_of_repeat = 0
            for b in itertools.repeat(reverse_b_idx,reverse_b):
                final_string += str(b)
                free_space_block_length -= 1
                num_of_repeat += 1
                if free_space_block_length <= 0 or len(final_string) >= length_of_final_string:
                    for reserve in itertools.repeat(reverse_b_idx, reverse_b-num_of_repeat):
                        reserve_stack.append(reserve)
                    break
            step += 1
    if len(final_string) >= length_of_final_string:
        break
    idx += 1

# checksum calculation
idx = 0
checksum = 0
for s in final_string:
    checksum += int(s) * idx
    idx += 1

# print(f"Final string: {final_string}")
print(len(final_string))
print(length_of_final_string)
print(f"Checksum: {checksum}")
print(f"Execution time: {time.time() - start_time} seconds")