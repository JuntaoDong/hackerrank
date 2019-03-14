# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumul(x, m, std):
    return 0.5 * (1 + math.erf((x - m)/(std*math.sqrt(2))))

tickets = int(input())
n = int(input())
m = float(input())
std = float(input())

print(round(cumul(tickets, n*m, math.sqrt(n)*std), 4))