import time
import numpy as np

DAY = 1
input = np.genfromtxt(f"day{DAY}/input.txt", delimiter="  ")
test = np.genfromtxt(f"day{DAY}/test_input.txt", delimiter="  ")

curr = input.copy()
#----------------------------------------
# experimenting with using numpy arrays for the first time 
start_time = time.time()
firstNum = curr[:,0]
secondNum = curr[:,1]

firstNum.sort()
secondNum.sort()

# Part 1: getting the distance between pairs
totalDistance = 0
for i in range(len(firstNum)):
    totalDistance += abs(firstNum[i] - secondNum[i]) 
print(f"Total Distance: {totalDistance}")

# Part 2: getting similarity score
totalSimilarity = 0
for i in range(len(firstNum)):
    # using count_nonzero to count number of occurences of an element in nparray
    number_of_occurrences = np.count_nonzero(secondNum == firstNum[i])
    totalSimilarity += firstNum[i] * number_of_occurrences
print(f"Total Distance: {totalSimilarity}")

print(f"Execution time: {time.time() - start_time} seconds")