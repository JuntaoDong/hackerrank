#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    lst = [0] * (n+1)
    total = 0
    temp = 0
    for query in queries:
        lst[query[0]-1] += query[2]
        lst[query[1]] -= query[2]
    for i in lst:
        temp += i
        if temp > total:
            total = temp
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
