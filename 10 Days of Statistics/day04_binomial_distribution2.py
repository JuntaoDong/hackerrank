# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def binomial(x, n, p):
    comb = math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
    return comb*((p/100)**x)*((1-(p/100))**(n-x))

p, n = map(int, input().strip().split())
print(round(sum(binomial(x,n,p) for x in range(3)), 3))
print(round(sum(binomial(x,n,p) for x in range(2,n+1)), 3))
