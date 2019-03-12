'''
Task
Given set S={1,2,3,...,N}. Find two integers, A and B (where A<B), from set S such that the value of A&B is the maximum possible and also less than a given integer, K. In this case, & represents the bitwise AND operator.

Input Format
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

Output Format
For each test case, print the maximum possible value of A&B on a new line.
'''

# Brute-force
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        max_value = 0

        for i in range(1, n):
            for j in range(i+1, n+1):
                output = i & j
                if output == k-1:
                    max_value = output
                    break

                elif output > max_value and output < k:
                    max_value = output

        print(max_value)


# Smarter way

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(k-1 if ((k-1) | k) <= n else k-2)

'''
When k is ODD , k-1 is EVEN , k-1 can always be reached by (k-1) & k.
In binary form:
    k   = 11
    k-1 = 10
    k-1 == (k-1) & k
That is ((k-1) | k) is always k. And ((k-1) | k) <= n is always TRUE.


When k is EVEN , k-1 is ODD , k-1 can only be reached only if ((k-1) | k) <= n is TRUE
In binary form:
    k   = 10110
    k-1 = 10101
    k|(k-1) = 10111
    k-1 == (k-1) & (k|(k-1))
We can always get k-1 from (k-1) & (k|(k-1)). (k|(k-1)) is larger than k, therefore, whenever n >= (k|(k-1)), we can always get k-1. Otherwise , you just need to follow the process above when k is ODD (because k-1 is ODD) , then you get the answer k-2.

In brief , you can just do the test ((k-1) | k) <= n to determine the answer.
'''
