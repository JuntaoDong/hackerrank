# Enter your code here. Read input from STDIN. Print output to STDOUT
def geo(n, p):
    return p*(1-p)**(n-1)

num, den = map(int, input().strip().split())
n = int(input())
print(round(sum(geo(i, num/den) for i in range(1,n+1)), 3))