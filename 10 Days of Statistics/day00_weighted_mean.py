# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(int, input().rstrip().split()))
W = list(map(int, input().rstrip().split()))
total = 0
for i in range(n):
    total += X[i] * W[i]
mean = total/sum(W)
print('%.1f' % mean)
