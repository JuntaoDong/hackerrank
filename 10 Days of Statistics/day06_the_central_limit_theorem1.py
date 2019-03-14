
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumul(x, m, std):
    return 0.5 * (1 + math.erf((x - m)/(std*math.sqrt(2))))

max_w = int(input())
n = int(input())
m = int(input())
std = int(input())

print(round(cumul(max_w, n*m, math.sqrt(n)*std), 4))