# Enter your code here. Read input from STDIN. Print output to STDOUT
def geo(n, p):
    return round(p*(1-p)**(n-1), 3)

num, den = map(int, input().strip().split())
insp = int(input())
print(geo(insp, num/den))
