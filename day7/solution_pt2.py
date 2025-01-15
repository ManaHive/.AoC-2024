import time
import numpy as np
import itertools

DAY = 7
with open(f'day{DAY}/input.txt') as i:
    input_nl = i.readlines()
input = np.array([l.strip('\n\r') for l in input_nl])
with open(f'day{DAY}/test_input.txt') as i:
    test_nl = i.readlines()
test= np.array([l.strip('\n\r') for l in test_nl])
curr = input.copy()
start_time = time.time()
#----------------------------------------
# PART 1: Find sum of calibration nums, get calibration nums from the equations that could possibly be true from the list (combination of + and *)
# Steps:
# Break down input into two lists, target calibration num and list of nums
# Use itertools product to find all combinations of operators from len of list of nums -1
# Construct all possible equations as a string and use eval to calculate

# PART 2: Guess we have a concatenation operator now || 
calibration_nums = []
equations = []
# processing input
for l in curr:
    split = l.split(": ")
    cal_num = int(split[0])
    eq = split[1].split(" ")
    calibration_nums.append(cal_num)
    equations.append(eq)

# I am a lazy bum and got ChatGPT to generate a function that evaluates equation strings left to right for me
# That probably was the point of the puzzle, oops
def evaluate_left_to_right(expression):
    # Split the expression into tokens
    tokens = expression.split()
    # Initialize result with the first number
    result = int(tokens[0])
    # Process the remaining tokens in pairs (operator, number)
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        number = int(tokens[i + 1])
        # Perform the operation based on the operator
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        elif operator == '/':
            result /= number
        elif operator == "|":
            result = int(str(result) + str(number))
    return result

lst_valid_num = []
for i in zip(calibration_nums,equations):
    cal_num = i[0]
    equation = i[1]
    length = len(i[1])
    lst_of_op_combos = list(itertools.product("+*|", repeat=length-1))
    # construct equation string
    for op in lst_of_op_combos:
        idx = 0
        eq_string = ""
        for n in equation:
            if idx < length-1:
                eq_string += n + " " +  op[idx] + " "
            else:
                eq_string += n
            idx += 1
        if evaluate_left_to_right(eq_string) == cal_num:
            lst_valid_num.append(cal_num)
            break

print(f"List of valid nums: {lst_valid_num}")
print(f"Sum: {sum(lst_valid_num)}")
print(f"Execution time: {time.time() - start_time} seconds")