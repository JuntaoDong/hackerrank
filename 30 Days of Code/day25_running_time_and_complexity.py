'''
Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code!

Input Format
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Output Format
For each test case, print whether n is Prime or Not prime on a new line.
'''

# trial division: Given an input number n, check whether any prime integer m from 2 to √n evenly divides n (the division leaves no remainder). If n is divisible by any m then n is composite, otherwise it is prime.
import math
def isPrime(num):
    if num == 1:
        print('Not prime')
    elif num < 1:
        raise ValueError('Please input positive integers')
    elif num == 2:
        print('Prime')
    else:
        for j in range(2, int(math.sqrt(num))+1):
            if num % j == 0:
                print('Not prime')
                return
        print('Prime')

n = int(input())
for i in range(n):
    num = int(input())
    isPrime(num)
