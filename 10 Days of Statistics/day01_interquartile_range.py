# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

N = int(input())
ele = list(map(int, input().rstrip().split()))
fre = list(map(int, input().rstrip().split()))
arr = []

for i in range(N):
    arr.extend([ele[i]]*fre[i])

arr.sort()
midpoint = sum(fre)//2
q1 = statistics.median(arr[:midpoint])
q3 = statistics.median(arr[-midpoint:])

print('%.1f' % (q3-q1))
