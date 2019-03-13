import math
def binomial(x, n, p):
    comb = math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
    return comb*(p**x)*((1-p)**(n-x))

boy, girl = map(float, input().strip().split())
p = boy/(boy+girl)
children = 6
boys = 3
prop = 0
for i in range(boys, children+1):
    prop += binomial(i, children, p)
print(round(prop, 3))
