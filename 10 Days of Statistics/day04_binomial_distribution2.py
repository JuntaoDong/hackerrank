# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def binomial(x, n, p):
    comb = math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
    return comb*(p**x)*((1-p)**(n-x))

p, n = map(float, input().strip().split())
p = p/100
prob = 0
for i in range(2):
    prob += binomial(i, n, p)
print(round(prob, 3))
print(1-round(prob, 3))
