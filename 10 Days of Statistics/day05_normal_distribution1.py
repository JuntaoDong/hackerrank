# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumul(x, m, std):
    return 0.5 * (1 + math.erf((x - m)/(std*math.sqrt(2))))
    
m, std = map(int, input().strip().split())
x0 = float(input())
x1, x2 = map(float, input().strip().split())

print(round(cumul(x0, m, std), 3))
print(round(cumul(x2, m, std) - cumul(x1, m, std), 3))