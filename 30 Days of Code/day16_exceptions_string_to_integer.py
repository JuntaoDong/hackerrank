'''
Task
Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language.

Input Format
A single string, S.

Output Format
Print the parsed integer value of , or Bad String if  cannot be converted to an integer.

'''

#!/bin/python3

import sys


S = input().strip()
try:
    print(int(S))
except ValueError:
    print('Bad String')
