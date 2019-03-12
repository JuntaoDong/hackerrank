'''
Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Input Format
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a String, S.

Output Format
For each String Sj (where 0<=j<=T-1), print Sj's even-indexed characters, followed by a space, followed by 's odd-indexed characters.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
age = int(input())

for i in range(age):
    s = str(input())
    s_even = str()
    s_odd = str()
    for j in range(len(s)):
        if j%2 == 0:
            s_even += s[j]
        else:
            s_odd += s[j]
    print(s_even, s_odd)
