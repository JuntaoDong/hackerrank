# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.

# Output Format
# Print the largest (maximum) hourglass sum found in A.

#!/bin/python3

import math
import os
import random
import re
import sys

# Solution 1

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            total = sum(arr[i][j:j+3]) + sum(arr[i+2][j:j+3]) + arr[i+1][j+1]
            max_sum.append(total)
print(max(max_sum))


# Solution 2

hg_shape = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]
print(max(sum(arr[i+x][j+y] for x, y in hg_shape) for i in range(4) for j in range(4)))
