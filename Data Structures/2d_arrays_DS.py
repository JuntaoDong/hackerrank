#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    lst = []
    for i in range(4):
        for j in range(4):
            lst.append(sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3]))
    return max(lst)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
