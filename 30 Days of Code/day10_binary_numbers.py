# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

# Input Format
# A single integer, n.

# Constraints
# 1 <= n <= 10e6

# Output Format
# Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

# Solution 1

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n = str(bin(n))[2:]

    lst = []

    for i in range(len(n)):
        count = 0
        while n[i] == '1':
            count += 1
            if i<len(n)-1:
                i += 1
            else:
                break
        lst.append(count)
    print(max(lst))


# Solution 2
if __name__ == '__main__':
    n = int(input())
    n = str(bin(n))[2:]
    lst1 = n.strip().split('0')
    lst2 = []
    for i in lst1:
        lst2.append(len(i))
    print(max(lst2))


# Solution 3
if __name__ == '__main__':
    print(len(max(bin(int(input().strip()))[2:].split('0'))))
