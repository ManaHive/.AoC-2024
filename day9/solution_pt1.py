import time
import numpy as np

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

lst_final_string = []
idx = 0
reserve_stack = []
length_of_file_blocks = len(file_blocks)
length_of_final_string = sum(file_blocks)

for f in file_blocks:
    to_append = min(f, length_of_final_string - len(lst_final_string))
    lst_final_string.extend([idx] * to_append)
    
    if len(lst_final_string) >= length_of_final_string:
        break
    if idx < len(free_space) - 1:
        free_space_block_length = free_space[idx]
        step = 0
        while (free_space_block_length > 0 and len(lst_final_string) < length_of_final_string):
            # check reserve stack first, then look at the back of file_blocks again
            while reserve_stack and free_space_block_length > 0:
                lst_final_string.append(reserve_stack.pop(0))
                free_space_block_length -= 1
                if len(lst_final_string) >= length_of_final_string:
                    break

            # Fill from reverse blocks
            if free_space_block_length > 0:
                reverse_b_idx = length_of_file_blocks - idx - step - 1

                reverse_b = file_blocks[reverse_b_idx]
                to_append = min(free_space_block_length, reverse_b, length_of_final_string - len(lst_final_string))
                lst_final_string.extend([reverse_b_idx] * to_append)
                free_space_block_length -= to_append

                # Update reserve stack for unused blocks
                reserve_stack.extend([reverse_b_idx] * (reverse_b - to_append))
                step += 1
                if len(lst_final_string) >= length_of_final_string:
                    break
    if len(lst_final_string) >= length_of_final_string:
        break
    idx += 1

checksum = 0
for idx, s in enumerate(lst_final_string):
    for repeat in str(s):
        checksum += s * idx
# print(f"Final string: {lst_final_string}")
print(length_of_final_string)
print(len(lst_final_string))
print(f"Checksum: {checksum}")
print(f"Execution time: {time.time() - start_time} seconds")