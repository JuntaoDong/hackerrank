# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumul(x, m, std):
    return 0.5 * (1 + math.erf((x - m)/(std*math.sqrt(2))))

m, std = map(int, input().strip().split())
x0 = int(input())
x1 = int(input())

print(round(100 * (1 - cumul(x0, m, std)), 2))
print(round(100 * (1- cumul(x1, m, std)), 2))
print(round(100 * cumul(x1, m, std), 2))