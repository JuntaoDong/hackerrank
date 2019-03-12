'''
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 * days late.
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 * months late.
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000.

Input Format
The first line contains  space-separated integers denoting the respective day, month, and year on which the book was actually returned.
The second line contains  space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

Output Format
Print a single integer denoting the library fine for the book received as input.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = list(map(int, input().strip().split()))
expected =list(map(int, input().strip().split()))

if actual[2]==expected[2] and actual[1]==expected[1] and actual[0]>expected[0]:
    print((actual[0]-expected[0])*15)
elif actual[2]==expected[2] and actual[1]>expected[1]:
    print((actual[1]-expected[1])*500)
elif actual[2]>expected[2]:
    print(10000)
else:
    print(0)
