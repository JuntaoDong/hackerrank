# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def poi(m, r):
    return (m**r)*math.exp(-m)/math.factorial(r)

m = float(input())
r = int(input())
print(round(poi(m, r), 3))