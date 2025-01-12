import time
import numpy as np

DAY = 2
#input = np.genfromtxt(f"day{DAY}/input.txt", delimiter=" ")

# input has uneven rows, so we gotta process this row by row.....
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
# rules for safe reports: 
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# getting number of safe reports

# PART 2:
# one single bad level is ok

# PART 2 SOLUTION
# function for evaluating the list of report nums
def eval(report_nums):
    print(report_nums)
    increasingFlag = False
    decreasingFlag = False
    diff = 0
    for n in range(len(report_nums)):
        # ensure no out-of-range errors
        if n+1 < len(report_nums):
            #check diff between n and n+1 to see if increasing or decreasing
            increasingFlag = True if report_nums[n+1]>report_nums[n] else increasingFlag
            decreasingFlag = True if report_nums[n+1]<report_nums[n] else decreasingFlag

            diff = report_nums[n+1] - report_nums[n]
            # failure conditions: increasingFlag and decreasingFlag both true, abs(diff) greater than 3, abs(diff) less than 1
            if (increasingFlag and decreasingFlag) or abs(diff) > 3 or abs(diff) < 1:
                print(f"index: {n} n:{report_nums[n]} n+1:{report_nums[n+1]} increasingFlag:{increasingFlag} deceasingFlag:{decreasingFlag} diff:{diff} ")
                # return the index of failure if well, it fails
                return n
    # return negative one if all is well
    return -1
    
num_of_safe = 0
for l in curr:
    # creating a list of report nums from the report string line
    successFlag = False
    report_nums = [int(num) for num in l.split(" ")]
    # evaluate full list for first time, then evaluate the list with one of each num removed
    if eval(report_nums) != -1:
        for n in range(len(report_nums)):
            curr = report_nums.copy()
            curr.pop(n)
            if eval(curr) == -1:
                successFlag = True
                break
    else:
        successFlag = True
    num_of_safe += 1 if successFlag else 0

print(f"Number of safe reports: {num_of_safe}")                
print(f"Execution time: {time.time() - start_time} seconds")