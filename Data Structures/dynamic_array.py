#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.


def dynamicArray(n, queries):
    lastAnswer = 0
    seqList = [[] for _ in range(n)]   # create empty dynamic array
    out = []
    for q in queries:
        if q[0] == 1:
            seqList[(q[1] ^ lastAnswer) % n].append(q[2])
        else:
            lastAnswer = seqList[(q[1] ^ lastAnswer) % n][q[2] %
                                                          len(seqList[(q[1] ^ lastAnswer) % n])]
            out.append(lastAnswer)
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()