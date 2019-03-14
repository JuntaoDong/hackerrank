# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
m = int(input())
std = int(input())
p = float(input())
z = float(input())

A = m - z * std/math.sqrt(n)
B = m + z * std/math.sqrt(n)

print(round(A, 2))
print(round(B, 2))
